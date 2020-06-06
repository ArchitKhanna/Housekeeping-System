from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import CorridorUpdateForm
import os
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
    )
from .models import (
                    Announcement,
                    apartment,
                    numberOfRooms,
                    livingRoom,
                    kitchen,
                    corridor,
                    bedroom,
                    ensuite,
                    bathroom,
                    taskslivingRoom,
                    tasksKitchen,
                    tasksCorridor,
                    tasksBedroom,
                    tasksEnsuite,
                    livingRoomCheckList,
                    kitchenCheckList,
                    corridorCheckList,
                    bedroomCheckList,
                    ensuiteCheckList
                    )
#On adding a new view, ensure it is rendering the right html page and has the
# right name along with variables data etc.

#METHOD BASED VIEWS

@login_required
def home(request):
    context = {
        'title': 'Home',
        'posts': Announcement.objects.all()
    }

    return render(request, 'HKmanager/home.html', context)

@login_required
def gdpr(request):
    context = {
        'title': 'GDPR',
    }

    return render(request, 'HKmanager/gdpr.html', context)

@login_required
def about(request):
    context = {
        'title': 'About Us',
    }

    return render(request, 'HKmanager/about.html', context)

@login_required
def tutorial(request):
    context = {
        'title': 'Tutorial'
    }
    return render(request, 'HKmanager/tutorial.html', context)

@login_required
def thomondvillage(request):
    context = {
        'apartment': apartment.objects.all(),
        'title': 'Thomond Village Panel'
    }
    return render(request, 'HKmanager/villagepanel.html', context)

@login_required
def setcallback(request, pk, list_id, key):

    def listAssigner(i):

        switcher = {
            1:livingRoomCheckList,
            2:kitchenCheckList,
            3:corridorCheckList,
            4:bedroomCheckList,
            5:ensuiteCheckList,
        }

        return switcher.get(i, "nothing")

    checkList = listAssigner(key)

    task = checkList.objects.get(pk=list_id)
    task.callback = True
    task.save()
    return redirect('/apartment/'+str(pk)+'/')

@login_required
def undocallback(request, pk, list_id, key):

    def listAssigner(i):

        switcher = {
            1:livingRoomCheckList,
            2:kitchenCheckList,
            3:corridorCheckList,
            4:bedroomCheckList,
            5:ensuiteCheckList,
        }

        return switcher.get(i, "nothing")

    checkList = listAssigner(key)

    task = checkList.objects.get(pk=list_id)
    task.callback = False
    task.save()
    return redirect('/apartment/'+str(pk)+'/')

@login_required
def complete(request, pk, list_id, key):

    def listAssigner(i):

        switcher = {
            1:livingRoomCheckList,
            2:kitchenCheckList,
            3:corridorCheckList,
            4:bedroomCheckList,
            5:ensuiteCheckList,
        }

        return switcher.get(i, "nothing")

    checkList = listAssigner(key)

    task = checkList.objects.get(pk=list_id)
    task.checked = True
    task.save()
    return redirect('/apartment/'+str(pk)+'/')

@login_required
def undocomplete(request, pk, list_id, key):

    def listAssigner(i):

        switcher = {
            1:livingRoomCheckList,
            2:kitchenCheckList,
            3:corridorCheckList,
            4:bedroomCheckList,
            5:ensuiteCheckList,
        }

        return switcher.get(i, "nothing")

    checkList = listAssigner(key)

    task = checkList.objects.get(pk=list_id)
    task.checked = False
    task.save()
    return redirect('/apartment/'+str(pk)+'/')

#CLASS BASED VIEWS

class AnnouncementListView(LoginRequiredMixin, ListView):
    model = Announcement
    template_name = 'HKmanager/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class AnnouncementDetailView(LoginRequiredMixin, DetailView):
    model = Announcement

class AnnouncementCreateView(LoginRequiredMixin, CreateView):
    model = Announcement
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class AnnouncementUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Announcement
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        announcement = self.get_object()
        if self.request.user == announcement.author or self.request.user.is_superuser:
            return True
        return False

class AnnouncementDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Announcement
    success_url = '/home/'

    def test_func(self):
        announcement = self.get_object()
        if self.request.user == announcement.author or self.request.user.is_superuser:
            return True
        return False


class ApartmentListView(LoginRequiredMixin, ListView):
    model = apartment
    template_name = 'HKmanager/villagepanel.html'
    context_object_name = 'apartment'
    paginate_by = 10

class ApartmentDetailView(LoginRequiredMixin, DetailView):
    model = apartment

    def get_context_data(self, *args, **kwargs):
        context = super(ApartmentDetailView, self).get_context_data(*args, **kwargs)
        bedrooms = bedroom.objects.filter(apartment=self.object.pk)
        ensuites = ensuite.objects.filter(apartment=self.object.pk)
        context["bedrooms"] = bedrooms
        context["livingRoomCheckList"] = livingRoomCheckList.objects.all().filter(livingroom=self.object.livingroom)
        context["kitchenCheckList"] = kitchenCheckList.objects.all().filter(kitchen=self.object.kitchen)
        context["corridorCheckList"] = corridorCheckList.objects.all().filter(corridor=self.object.corridor)

        allRoomsCheckList = []
        allEnsuitesCheckList = []

        for room in bedrooms:
            allRoomsCheckList+= bedroomCheckList.objects.all().filter(bedroom=room)

        for ens in ensuites:
            allEnsuitesCheckList+= ensuiteCheckList.objects.all().filter(ensuite=ens)

        context["bedroomCheckList"] = allRoomsCheckList
        context["ensuiteCheckList"] = allEnsuitesCheckList
        return context

class ApartmentCreateView(LoginRequiredMixin, CreateView):
    model = apartment
    fields = ['number', 'block', 'rooms', 'status', 'task', 'assignee']

    def get_context_data(self, *args, **kwargs):
        context = super(ApartmentCreateView, self).get_context_data(*args, **kwargs)
        legend = "Add New Apartment"
        btn = "Add Apartment"
        update = False
        context["legend"] = legend
        context["btn"] = btn
        context["update"] = update
        return context

class ApartmentUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = apartment
    fields = ['status', 'task', 'assignee']

    def test_func(self):
        apartment = self.get_object()
        if self.request.user == apartment.assignee or self.request.user.is_superuser:
            return True
        return False

    def get_context_data(self, *args, **kwargs):
        context = super(ApartmentUpdateView, self).get_context_data(*args, **kwargs)
        legend = "Update Apartment"
        btn = "Update"
        update = True
        context["legend"] = legend
        context["btn"] = btn
        context["update"] = update
        return context

class ApartmentDeleteView(LoginRequiredMixin, DeleteView):
    model = apartment
    success_url = '/thomondvillage/'

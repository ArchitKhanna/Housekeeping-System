from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
    )
from .models import (
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

@login_required
def home(request):
    context = {
        'title': 'Housekeeper'
    }
    return render(request, 'HKmanager/home.html', context)

#class MyApartmentListView(ListView):
#    model = apartment
#    template_name = 'HKmanager/home.html'

@login_required
def tutorial(request):
    context = {
        'title': 'Housekeeper - Tutorial'
    }
    return render(request, 'HKmanager/tutorial.html', context)

@login_required
def thomondvillage(request):
    context = {
        'apartment': apartment.objects.all(),
        'title': 'Thomond Village Panel'
    }
    return render(request, 'HKmanager/thomondvillage.html', context)

class ApartmentListView(LoginRequiredMixin, ListView):
    model = apartment
    template_name = 'HKmanager/ThomondVillage.html'
    context_object_name = 'apartment'

class ApartmentDetailView(LoginRequiredMixin, DetailView):
    model = apartment

    def get_context_data(self, *args, **kwargs):
        context = super(ApartmentDetailView, self).get_context_data(*args, **kwargs)
        bedrooms = bedroom.objects.filter(apartment=self.object.pk)
        context["bedrooms"] = bedrooms
        context["livingRoomCheckList"] = livingRoomCheckList.objects.all().filter(livingroom=self.object.livingroom)
        context["kitchenCheckList"] = kitchenCheckList.objects.all().filter(kitchen=self.object.kitchen)
        context["corridorCheckList"] = corridorCheckList.objects.all().filter(corridor=self.object.corridor)
        allRoomsCheckList = []
        for room in bedrooms:
            allRoomsCheckList+= bedroomCheckList.objects.all().filter(bedroom=room)

        context["bedroomCheckList"] = allRoomsCheckList
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

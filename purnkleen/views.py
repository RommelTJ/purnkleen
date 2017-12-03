from django.shortcuts import render


def home(request):
    return render(request, "index.html", {})

def giveaway(request):
    return render(request, 'giveaway.html', {})


#########################
# Start About Views     #
#########################
def about(request):
    return render(request, 'about.html', {})


def vision(request):
    return render(request, 'vision.html', {})


def values(request):
    return render(request, 'values.html', {})


def team(request):
    return render(request, 'team.html', {})


def benefits(request):
    return render(request, 'benefits.html', {})


def bylaws(request):
    return render(request, 'bylaws.html', {})


def join(request):
    return render(request, 'join.html', {})
#########################
# End About Views       #
#########################


#########################
# Start Solutions Views #
#########################
def mission_planner(request):
    return render(request, 'mission-planner.html', {})


def fleet_view(request):
    return render(request, 'fleet-view.html', {})
#########################
# End Solutions Views   #
#########################


#########################
# Start Services Views  #
#########################
def fuel_services(request):
    return render(request, 'fuel-services.html', {})


def maintenance_repair(request):
    return render(request, 'maintenance-and-repair.html', {})


def transportation(request):
    return render(request, 'transportation.html', {})
#########################
# End Services Views    #
#########################


#########################
# Start Knowledge Views #
#########################
def links_tools(request):
    return render(request, 'links-and-tools.html', {})
#########################
# End Knowledge Views   #
#########################
from django.shortcuts import render, redirect
from .models import SupportTicket
from .forms import SupportTicketForm
from django.shortcuts import get_object_or_404

def dashboard(request):
    total_tickets = SupportTicket.objects.count()

    open_tickets = SupportTicket.objects.filter(
        status='Open'
    ).count()

    in_progress_tickets = SupportTicket.objects.filter(
        status='In Progress'
    ).count()

    resolved_tickets = SupportTicket.objects.filter(
        status='Resolved'
    ).count()

    recent_tickets = SupportTicket.objects.order_by('-created_at')[:5]

    context = {
        'total_tickets': total_tickets,
        'open_tickets': open_tickets,
        'in_progress_tickets': in_progress_tickets,
        'resolved_tickets': resolved_tickets,
        'recent_tickets': recent_tickets,
    }

    return render(request, 'helpdesk/dashboard.html', context)


def ticket_create(request):
    if request.method == 'POST':
        form = SupportTicketForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    else:
        form = SupportTicketForm()

    context = {
        'form': form
    }

    return render(request, 'helpdesk/ticket_create.html', context)


def ticket_list(request):
    search_query = request.GET.get('search', '')
    status_filter = request.GET.get('status', '')
    priority_filter = request.GET.get('priority', '')

    tickets = SupportTicket.objects.all().order_by('-created_at')

    if search_query:
        tickets = tickets.filter(subject__icontains=search_query)

    if status_filter:
        tickets = tickets.filter(status=status_filter)

    if priority_filter:
        tickets = tickets.filter(priority=priority_filter)

    context = {
        'tickets': tickets,
        'search_query': search_query,
        'status_filter': status_filter,
        'priority_filter': priority_filter,
    }

    return render(request, 'helpdesk/ticket_list.html', context)


def ticket_detail(request, id):
    ticket = get_object_or_404(SupportTicket, id=id)

    context = {
        'ticket': ticket
    }

    return render(request, 'helpdesk/ticket_detail.html', context)

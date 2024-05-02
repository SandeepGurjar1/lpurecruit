from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from hr.models import JobPost , CandidateApplications , SelectCandidateJob, Hr
# from candidate.models import IsSortList
# # Create your views here.

@login_required
def hrHome_views(request):
    if Hr.objects.filter(user=request.user).exists():
        jobpost = JobPost.objects.filter(user=request.user)
        print(jobpost)
        return render(request,'hr/hrdashboard.html',{'jobpost':jobpost})
    return redirect('candidate_dashboard')

@login_required
def post_job_views(request):
    msg = None
    if request.method == 'POST':
        job_title = request.POST.get('job-title')
        address = request.POST.get('address')
        company_name = request.POST.get('company-name')
        salary_low = request.POST.get('salary-low')
        salary_high = request.POST.get('salary-high')
        last_date  = request.POST.get('last-date')
        print(job_title+" "+address+ " "+company_name)
        msg = "Job added.."
        jobpost = JobPost(user=request.user,title=job_title,address=address,companyName=company_name,salaryLow=salary_low,salaryHigh=salary_high,lastDateToApply=last_date)
        jobpost.save()
    return render(request,'hr/postjob.html',{'msg':msg})
   
@login_required
def candidate_view(request,pk):
    if JobPost.objects.filter(id=pk).exists():
        job = JobPost.objects.get(id=pk)
        applications = CandidateApplications.objects.filter(job=job)
        selectedapplications = SelectCandidateJob.objects.filter(job=job)
        return render(request, 'hr/candidate.html',{'applications':applications,'selectedapplications':selectedapplications,'jobpost':job})
    return redirect('hr_dash')

@login_required
def selectCandidate(request):
    if request.method == 'POST':
        candidateid = request.POST.get('candidateid')
        jobpostid = request.POST.get('jobpostid')
        job = JobPost.objects.get(id=jobpostid)
        candidate = CandidateApplications.objects.get(id=candidateid)
        SelectCandidateJob(job=job, candidate=candidate).save()
        
    return redirect('hr_dash')

@login_required
def deleteCandidate(request):
    if request.method == 'POST':
        candidateid = request.POST.get('candidateid')
        jobpostid = request.POST.get('jobpostid')
        job = JobPost.objects.get(id=jobpostid)
        candidate = CandidateApplications.objects.get(id=candidateid).delete()
        job.applyCount = job.applyCount -1
        job.save()
    return redirect('hr_dash')


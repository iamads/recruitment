from myapp.models import Candidate
from myapp.models import Recruiter
from serializers import CandidateSerializer
class CandidateLib():

	def add_candidate(self, candidate_details):
		Candidate.objects.create(**candidate_details)

	def get_candidate(self, options):
		candidate_id = options.GET.get('candidate_id')
		if candidate_id:
			candidates = Candidate.objects.get(candidate_id=candidate_id)
		else:
			candidates = Candidate.objects.get_all()
		return CandidateSerializer(candidates).data

	def update_candidate(self, modifications):
		candidate_id = modifications.get('candidate_id')
		candidate = Candidate.objects.get(candidate_id=candidate_id)

		if 'name' in modifications:
			candidate.candidate_name = modifications['name']

		if 'password' in modifications:
			candidate.password = modifications['password']

		if 'recruiter' in modifications:
			recruiter_id = modifications['recruiter']
			recruiter = Recruiter.objects.get(recruiter_id=recruiter_id)
			candidate.recruiter = recruiter
		candidate.save()

	def delete_candidate(self, options):
		candidate_id = options.GET.get('candidate_id')
		candidate = Candidate.objects.get(candidate_id=candidate_id)
		candidate.delete()
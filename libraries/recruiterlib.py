from myapp.models import Recruiter
from serializers import RecruiterSerializer
class RecruiterLib():

	def add_recruiter(self, recruiter_details):
		Recruiter.objects.create(**recruiter_details)

	def get_recruiter(self, options):
		recruiter_id = options.GET.get('recruiter_id')
		if recruiter_id:
			recruiters = Recruiter.objects.get(recruiter_id=recruiter_id)
		else:
			recruiters = Recruiter.objects.get_all()
		return RecruiterSerializer(recruiters).data

	def update_recruiter(self, modifications, options):
		recruiter_id = options.GET.get('recruiter_id')
		recruiter = Recruiter.objects.get(recruiter_id=recruiter_id)

		if 'name' in modifications:
			recruiter.recruiter_name = modifications['name']

		if 'password' in modifications:
			recruiter.password = modifications['password']

		recruiter.save()

	def delete_recruiter(self, options):
		recruiter_id = options.GET.get('recruiter_id')
		recruiter = Recruiter.objects.get(recruiter_id=recruiter_id)
		recruiter.delete()

from django.db import models
from django.contrib.auth.models import User

# models syntax:
#-------------------------
# modelData for instance
# modelCrossTable for cross table

# available data models
#-------------------------
# Focus issues
# Specialties
# Approaches
# State
# Language
# Schools


class LanguageData(models.Model):
	language 		= models.CharField(max_length=200)
	def __str__(self):
		return self.language

class LanguagesCrossTable(models.Model):
	language 		= models.ForeignKey(LanguageData	, on_delete=models.CASCADE, related_name="users")
	user 			= models.ForeignKey(User			, on_delete=models.CASCADE, related_name="languages")
	def __str__(self):
		return "Language" + str(self.language)

	def getId(self):
		return self.language.id

	@classmethod
	def update_user(cls, user, new_list):
		old_list = user.practitioner.get_languages()
		for language_id in old_list:
			if not language_id in new_list:
				cls.objects.get(user = user, language = LanguageData.objects.get(id = language_id)).delete()
		for language_id in new_list:
			cls.objects.get_or_create(user = user, language =  LanguageData.objects.get(id = language_id))

class FocusIssueData(models.Model):
	focus_issue 	= models.CharField(max_length=200)
	def __str__(self):
		return self.focus_issue

class FocusIssuesCrossTable(models.Model):
	focus_issue 	= models.ForeignKey(FocusIssueData	, on_delete=models.CASCADE, related_name="users")
	user			= models.ForeignKey(User			, on_delete=models.CASCADE, related_name="focus_issues")
	def __str__(self):
		return str(self.focus_issue)

	def getId(self):
		return self.focus_issue.id

	@classmethod
	def update_user(cls, user, new_list):
		old_list = user.practitioner.get_focus_issues()
		for focus_issue_id in old_list:
			if not focus_issue_id in new_list:
				cls.objects.get(user = user, focus_issue = FocusIssueData.objects.get(id = focus_issue_id)).delete()
		for focus_issue_id in new_list:
			cls.objects.get_or_create(user = user, focus_issue =  FocusIssueData.objects.get(id = focus_issue_id))

class SpecialtyData(models.Model):
	specialty 	= models.CharField(max_length=200)
	def __str__(self):
		return self.specialty

class SpecialtiesCrossTable(models.Model):
	specialty 		= models.ForeignKey(SpecialtyData	, on_delete=models.CASCADE, related_name="users")
	user			= models.ForeignKey(User			, on_delete=models.CASCADE, related_name="specialties")
	def __str__(self):
		return str(self.specialty)

	def getId(self):
		return self.specialty.id

	@classmethod
	def update_user(cls, user, new_list):
		old_list = user.practitioner.get_specialties()
		for specialty_id in old_list:
			if not specialty_id in new_list:
				cls.objects.get(user = user, specialty = SpecialtyData.objects.get(id = specialty_id)).delete()
		for specialty_id in new_list:
			cls.objects.get_or_create(user = user, specialty =  SpecialtyData.objects.get(id = specialty_id))

class ApproachData(models.Model):
	approach 		= models.CharField(max_length=200)
	def __str__(self):
		return self.approach

class ApproachesCrossTable(models.Model):
	approach 		= models.ForeignKey(ApproachData	, on_delete=models.CASCADE, related_name="users")
	user			= models.ForeignKey(User			, on_delete=models.CASCADE, related_name="approaches")
	def __str__(self):
		return str(self.approach)

	def getId(self):
		return self.approach.id

	@classmethod
	def update_user(cls, user, new_list):
		old_list = user.practitioner.get_approaches()
		for approach_id in old_list:
			if not approach_id in new_list:
				cls.objects.get(user = user, approach = ApproachData.objects.get(id = approach_id)).delete()
		for approach_id in new_list:
			cls.objects.get_or_create(user = user, approach =  ApproachData.objects.get(id = approach_id))

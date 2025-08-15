from rest_framework import serializers
from .models import AssignmentSubmission,Assignment
class AssignmentSerializer(serializers.ModelSerializer):
    description = serializers.CharField(
        max_length=500, allow_blank=True, required=False,
        style={'base_template': 'textarea.html'}
    )
    class Meta:
        model  = Assignment
        fields = ["id", "name", "description", "date_due", "max_points", "assignment_file"]

class AssignmentSubmissionSerializer(serializers.ModelSerializer):
    student_username = serializers.CharField(source="student.username", read_only=True)
    graded_by_name   = serializers.CharField(source="graded_by.username", read_only=True,allow_null=True,default=None,)
    assignment_max_points    = serializers.IntegerField(
        source="assignment.max_points", 
        read_only=True
    )
    assignment_name = serializers.CharField(source="assignment.name",read_only=True)
    class Meta:
        model  = AssignmentSubmission
        fields = [
            "id",
            "assignment",
            "assignment_max_points",
            "student_username",
            "submitted_at",
            "student_file",
            "student_points",
            "graded_at",
            "graded_by_name",
            "feedback",
            "assignment_name"
        ]
        read_only_fields = [
            "id",
            "submitted_at",
            "assignment",
            "student_username",
            "graded_at",
            "graded_by_name",
            "assignment_max_points",
            "assignment_name"
        ]


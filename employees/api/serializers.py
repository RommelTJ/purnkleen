from rest_framework import serializers

from accounts.api.serializers import UserDisplaySerializer
from employees.models import Employee


class StdImageFieldSerializer(serializers.ImageField):
    """
    Get all the variations of the StdImageField
    """

    def to_native(self, obj):
        return self.get_variations_urls(obj)

    def to_representation(self, obj):
        return self.get_variations_urls(obj)

    def get_variations_urls(self, obj):
        """
        Get all the logo urls.
        """

        # Initiate return object
        return_object = {}

        # Get the field of the object
        field = obj.field

        # A lot of ifs going around, first check if it has the field variations
        if hasattr(field, 'variations'):
            # Get the variations
            variations = field.variations
            # Go through the variations dict
            for key in variations.keys():
                # Just to be sure if the stdimage object has it stored in the obj
                if hasattr(obj, key):
                    # get the by stdimage properties
                    field_obj = getattr(obj, key, None)
                    if field_obj and hasattr(field_obj, 'url'):
                        # store it, with the name of the variation type into our return object
                        return_object[key] = super(StdImageFieldSerializer, self).to_representation(field_obj)

        # Also include the original (if possible)
        try:
            if hasattr(obj, 'url'):
                return_object['original'] = super(StdImageFieldSerializer, self).to_representation(obj)
        except ValueError:
            pass

        return return_object


class EmployeeModelSerializer(serializers.ModelSerializer):
    user = UserDisplaySerializer(read_only=True)
    primary_activity = serializers.SerializerMethodField()
    secondary_activity = serializers.SerializerMethodField()
    type = serializers.SerializerMethodField()
    image = StdImageFieldSerializer()

    def get_primary_activity(self, obj):
        return Employee.ACTIVITY_DICT[obj.primary_activity]

    def get_secondary_activity(self, obj):
        return Employee.ACTIVITY_DICT[obj.secondary_activity]

    def get_type(self, obj):
        return Employee.EMPLOYEE_DICT[obj.type]

    class Meta:
        model = Employee
        fields = "__all__"

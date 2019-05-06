from rest_framework.views import APIView
from django.http import JsonResponse


class GetTaxonomySchema(APIView):
    def get(self, request, *args, **kwargs):
        sections = self.get_base_queryset()
        all_data = []
        for section in sections:
            section_data = dict()
            section_data["instance"] = section
            section_data["children"] = section.get_categories_hierarchy()
            all_data.append(section_data)
        return JsonResponse(data=all_data, safe=False)

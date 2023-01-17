from django import forms
from .models import Device, DeviceName, StatusName, BrandName, GroupName, ModelName


class CreateForm(forms.Form):
    # title = forms.CharField(
    #     label="عنوان",
    #     min_length=2,
    #     max_length=255,
    #     required=True,
    #     widget=forms.TextInput(
    #         attrs={
    #             "placeholder": "عنوان را به انگلیسی وارد نمایید",
    #             "class": "form-control en",
    #         }
    #     )
    # )
    # title_fa = forms.CharField(
    #     label="عنوان به فارسی",
    #     min_length=2,
    #     max_length=255,
    #     required=True,
    #     widget=forms.TextInput(
    #         attrs={
    #             "placeholder": "عنوان را به فارسی وارد نمایید",
    #             "class": "form-control",
    #         }
    #     )
    # )
    # description = forms.CharField(
    #     label="توضیحات",
    #     required=False,
    #     widget=forms.Textarea(
    #         attrs={
    #             "placeholder": "توضیحات را وارد نمایید",
    #             "class": "form-control",
    #             "rows": "3",
    #         }
    #     )
    # )

    name = forms.ModelChoiceField(
        label='نام دستگاه',
        queryset=DeviceName.objects.filter(),
        required=True,
        empty_label="لطفا انتخاب نمایید",
        initial=None,
        widget=forms.Select(
            attrs={
                "placeholder": "نام دستگاه را انتخاب نمایید",
                "class": "form-control"
            }
        )
    )
    model = forms.ModelChoiceField(
        label='مدل دستگاه',
        queryset=ModelName.objects.filter(),
        required=True,
        empty_label="لطفا انتخاب نمایید",
        initial=None,
        widget=forms.Select(
            attrs={
                "placeholder": "مدل دستگاه را انتخاب نمایید",
                "class": "form-control"
            }
        )
    )
    status = forms.ModelChoiceField(
        label='وضعیت دستگاه',
        queryset=StatusName.objects.filter(),
        required=True,
        empty_label="لطفا انتخاب نمایید",
        initial=None,
        widget=forms.Select(
            attrs={
                "placeholder": "وضعیت دستگاه را انتخاب نمایید",
                "class": "form-control"
            }
        )
    )
    brand = forms.ModelChoiceField(
        label='شرکت سازنده',
        queryset=BrandName.objects.filter(),
        required=True,
        empty_label="لطفا انتخاب نمایید",
        initial=None,
        widget=forms.Select(
            attrs={
                "placeholder": "شرکت سازنده را انتخاب نمایید",
                "class": "form-control"
            }
        )
    )
    group = forms.ModelChoiceField(
        label='گروه دستگاه',
        queryset=GroupName.objects.filter(),
        required=True,
        empty_label="لطفا انتخاب نمایید",
        initial=None,
        widget=forms.Select(
            attrs={
                "placeholder": "گروه دستگاه را انتخاب نمایید",
                "class": "form-control"
            }
        )
    )
    regular_checks = forms.IntegerField(
        label="دوره های زمانی سرویس",
        required=False,
        widget=forms.NumberInput(
            attrs={
                "placeholder": "دوره های زمانی سرویس(برحسب ماه)",
                "class": "form-control"
            }
        )
    )
    description = forms.CharField(
        label="توضیحات",
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "توضیحات را وارد نمایید",
                "class": "form-control",
                "rows": "3",
            }
        )
    )


# class CreateForm(forms.ModelForm):
#     class Meta:
#         model = Device
#         fields = '__all__'

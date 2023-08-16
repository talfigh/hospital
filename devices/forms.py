from django import forms
from jdatetime import datetime

from devices.models import Device, DeviceName, StatusName, BrandName, GroupName, ModelName, DeviceLog


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
    next_check_at = forms.CharField(
        label="زمان سرویس بعدی",
        required=False,
        widget=forms.TextInput(
                    attrs={
                        "placeholder": "زمان سرویس بعدی",
                        "class": "form-control date-picker"
                    }
                )
        )
    next_check_at_en = forms.CharField(
        required=False
    )
    # next_check_at = forms.DateTimeInput(
    #     label="زمان سرویس بعدی",
    #     required=False,
    #     widget=forms.DateTimeField(
    #         attrs={
    #             "placeholder": "زمان سرویس بعدی",
    #             "class": "form-control"
    #         }
    #     )
    # )
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


class LogForm(forms.Form):
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

    phone_num = forms.IntegerField(
        label='شماره تماس',
        required=False,
        widget=forms.NumberInput(
            attrs={
                "placeholder": "لطفا شماره تماس را وارد کنید",
                "class": "form-control",
            }
        )
    )

    address = forms.CharField(
        label='آدرس',
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "لطفا آدرس را وارد کنید",
                "class": "form-control",
                "rows": "2",
            }
        )
    )

    name = forms.CharField(
        label='نام تحویل گیرنده',
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "لطفا نام را وارد کنید",
                "class": "form-control",
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

from mezzanine.conf import register_setting

register_setting(
    name="ADDRESS_STREET_1",
    description="Enter first street line or leave blank to ignore",
    editable=True,
    default="Bay Tree Cottage",
)

register_setting(
    name="ADDRESS_STREET_2",
    description="Street 2 or leave blank to ignore",
    editable=True,
    default="Sherborne Lane",
)

register_setting(
    name="ADDRESS_AREA",
    description="Area or leave blank to ignore",
    editable=True,
    default="Lyme Regis",
)

register_setting(
    name="ADDRESS_CITY",
    description="City or leave blank to ignore",
    editable=True,
    default="Dorset",
)

register_setting(
    name="ADDRESS_COUNTRY",
    description="Country or leave blank to ignore",
    editable=True,
    default="England",
)

register_setting(
    name="ADDRESS_POSTCODE",
    description="Post code or leave blank to ignore",
    editable=True,
    default="DT7 3NY",
)

register_setting(
    name="ADDRESS_MOBILE_NUMBER",
    description="Mobile Phone Number or leave blank to ignore",
    editable=True,
    default="07796-181882",
)

register_setting(
    name="ADDRESS_OTHER_NUMBER",
    description="Other Phone Number or leave blank to ignore",
    editable=True,
    default="01420-520375",
)

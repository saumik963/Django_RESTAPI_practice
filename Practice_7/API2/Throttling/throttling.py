from rest_framework.throttling import UserRateThrottle

class CustomeRateThrottle(UserRateThrottle):
    scope='custome'
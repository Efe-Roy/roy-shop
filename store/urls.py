from django.urls import path 
from .views import (CheckoutView, ItemDetail, HomeView, add_to_cart, 
                    remove_from_cart, OrderSummaryView, remove_single_item_from_cart,
                    PaymentView, AddCouponView, RequestRefundView, CategoryDetail,
                    LandingPage
)
app_name = "store"

urlpatterns = [
    path("", LandingPage, name="landpage"),
    path("home/", HomeView.as_view(), name="home"),
    path("checkout/", CheckoutView.as_view(), name="checkout"),
    path("order-summary/", OrderSummaryView.as_view(), name="order-summary"),
    path("product/<slug>", ItemDetail.as_view(), name="product"),
    path("add-to-cart/<slug>", add_to_cart, name="add-to-cart"),
    path("add-coupon", AddCouponView.as_view(), name="add-coupon"),
    path("remove-from-cart/<slug>", remove_from_cart, name="remove-from-cart"),
    path("remove-single-item-from-cart/<slug>", remove_single_item_from_cart, name="remove-single-item-from-cart"),
    path("payment/<payment_option>", PaymentView.as_view(), name="payment"),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),

    path('categorydetail/<slug>', CategoryDetail, name='categorydetail')
]
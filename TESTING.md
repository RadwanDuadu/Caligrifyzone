# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| about | [about.html](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/about/templates/about/about.html) | [Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcaligrifyzone-90b1cd839db0.herokuapp.com%2Fabout) | ![screenshot](documentation/validation/html-about-about.png) | No errors |
| about | [faq.html](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/about/templates/about/faq.html) | [Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcaligrifyzone-90b1cd839db0.herokuapp.com%2Fabout%2Ffaq) | ![screenshot](documentation/validation/html-about-faq.png) | No errors |
| about | [newsletter.html](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/about/templates/about/newsletter.html) | [Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcaligrifyzone-90b1cd839db0.herokuapp.com%2Fabout%2Fnewsletter) | ![screenshot](documentation/validation/html-about-newsletter.png) | No errors |
| bag | [bag.html](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/bag/templates/bag/bag.html) | [Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcaligrifyzone-90b1cd839db0.herokuapp.com%2Fbag) | ![screenshot](documentation/validation/html-bag-bag.png) | warning for addition of js script ignored as it doesn't effect implementation |
| checkout | [checkout.html](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/checkout/templates/checkout/checkout.html) | [Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcaligrifyzone-90b1cd839db0.herokuapp.com%2Fcheckout) | ![screenshot](documentation/validation/html-checkout-checkout.png) | one model error due to use of h5 title element, this is not added by developer and not effecting overall functionality |
| checkout | [checkout_success.html](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/checkout/templates/checkout/checkout_success.html) | [Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcaligrifyzone-90b1cd839db0.herokuapp.com%2Fcheckout%2Fcheckout_success%2F2E88FEFA8BF442E190165C244422FFC7) | ![screenshot](documentation/validation/html-checkout-checkout_success.png) | No errors |
| home | [index.html](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/home/templates/home/index.html) | [Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcaligrifyzone-90b1cd839db0.herokuapp.com%2F) | ![screenshot](documentation/validation/html-home-index.png) | No Errors |
| products | [add_product.html](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/products/templates/products/add_product.html) | [Link](https://validator.w3.org/nu/?level=warning&doc=https%3A%2F%2Fcaligrifyzone-90b1cd839db0.herokuapp.com%2Fproducts%2Fadd%2F) | ![screenshot](documentation/validation/html-products-add_product.png) | No errors |
| products | [edit_product.html](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/products/templates/products/edit_product.html) | [Link](https://validator.w3.org/nu/?level=warning&doc=https%3A%2F%2Fcaligrifyzone-90b1cd839db0.herokuapp.com%2Fproducts%2Fedit%2F1) | ![screenshot](documentation/validation/html-products-edit_product.png) | No errors|
| products | [product_detail.html](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/products/templates/products/product_detail.html) | [Link](https://validator.w3.org/nu/?level=warning&doc=https%3A%2F%2Fcaligrifyzone-90b1cd839db0.herokuapp.com%2Fproducts%2F1) | ![screenshot](documentation/validation/html-products-product_detail.png) | one model error due to use of h5 title element, this is not added by developer and not effecting overall functionality |
| products | [products.html](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/products/templates/products/products.html) | [Link](https://validator.w3.org/nu/?level=warning&doc=https%3A%2F%2Fcaligrifyzone-90b1cd839db0.herokuapp.com%2Fproducts) | ![screenshot](documentation/validation/html-products-products.png) | one model error due to use of h5 title element, this is not added by developer and not effecting overall functionality |
| profiles | [profile.html](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/profiles/templates/profiles/profile.html) | [Link](https://validator.w3.org/nu/?level=warning&doc=https%3A%2F%2Fcaligrifyzone-90b1cd839db0.herokuapp.com%2Fprofile) | ![screenshot](documentation/validation/html-profiles-profile.png) | No errors |
| templates | [login.html](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/templates/allauth/account/login.html) | [Link](https://validator.w3.org/nu/?level=warning&doc=https%3A%2F%2Fcaligrifyzone-90b1cd839db0.herokuapp.com%2Faccounts%2Flogin) | ![screenshot](documentation/validation/html-login.png) | No Errors |
| templates | [logout.html](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/templates/allauth/account/logout.html) | [Link](https://validator.w3.org/nu/?level=warning&doc=https%3A%2F%2Fcaligrifyzone-90b1cd839db0.herokuapp.com%2Faccounts%2Flogout) | ![screenshot](documentation/validation/html-logout.png) | No Errors |
| templates | [signup.html](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/templates/allauth/account/signup.html) | [Link](https://validator.w3.org/nu/?level=warning&doc=https%3A%2F%2Fcaligrifyzone-90b1cd839db0.herokuapp.com%2Faccounts%2Fsignup%2F) | ![screenshot](documentation/validation/html-signup.png) | No Errors |
| templates | [404.html](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/templates/errors/404.html) | No Link | ![screenshot](documentation/validation/html-templates-404.png) | No errors |


### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| checkout | [checkout.css](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/checkout/static/checkout/css/checkout.css) | No Link | ![screenshot](documentation/validation/css-checkout-checkout.png) | No Errors |
| profiles | [profile.css](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/profiles/static/profiles/css/profile.css) | No Link| ![screenshot](documentation/validation/css-profiles-profile.png) | No Errors |
| static | [base.css](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/static/css/base.css) | No Link | ![screenshot](documentation/validation/css-static-base.png) | No errors |


### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| checkout | [stripe_elements.js](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/checkout/static/checkout/js/stripe_elements.js) | No Link | ![screenshot](documentation/validation/js-checkout-stripe_elements.png) | stripe declaration found in other files |
| profiles | [countryfield.js](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/profiles/static/profiles/js/countryfield.js) | No Link | ![screenshot](documentation/validation/js-profiles-countryfield.png) | No Errors |


### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| about | [admin.py](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/about/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/Caligrifyzone/main/about/admin.py) | ![screenshot](documentation/validation/py-about-admin.png) | No Errors |
| about | [forms.py](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/about/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/Caligrifyzone/main/about/forms.py) | ![screenshot](documentation/validation/py-about-forms.png) | No Errors |
| about | [models.py](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/about/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/Caligrifyzone/main/about/models.py) | ![screenshot](documentation/validation/py-about-models.png) | No Errors |
| about | [test_forms.py](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/about/test_forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/Caligrifyzone/main/about/test_forms.py) | ![screenshot](documentation/validation/py-about-test_forms.png) | No Errors |
| about | [test_views.py](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/about/test_views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/Caligrifyzone/main/about/test_views.py) | ![screenshot](documentation/validation/py-about-test_views.png) | No Errors |
| about | [tests.py](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/about/tests.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/Caligrifyzone/main/about/tests.py) | ![screenshot](documentation/validation/py-about-tests.png) | No Errors |
| about | [urls.py](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/about/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/Caligrifyzone/main/about/urls.py) | ![screenshot](documentation/validation/py-about-urls.png) | No Errors |
| about | [views.py](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/about/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/Caligrifyzone/main/about/views.py) | ![screenshot](documentation/validation/py-about-views.png) | No Errors |
| bag | [admin.py](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/bag/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/Caligrifyzone/main/bag/admin.py) | ![screenshot](documentation/validation/py-bag-admin.png) | No Errors |
| bag | [contexts.py](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/bag/contexts.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/Caligrifyzone/main/bag/contexts.py) | ![screenshot](documentation/validation/py-bag-contexts.png) | No Errors |
| bag | [models.py](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/bag/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/Caligrifyzone/main/bag/models.py) | ![screenshot](documentation/validation/py-bag-models.png) | No Errors |
| bag | [bag_tools.py](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/bag/templatetags/bag_tools.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/Caligrifyzone/main/bag/templatetags/bag_tools.py) | ![screenshot](documentation/validation/py-bag-bag_tools.png) | No Errors |
| bag | [test_views.py](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/bag/test_views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/Caligrifyzone/main/bag/test_views.py) | ![screenshot](documentation/validation/py-bag-test_views.png) | No Errors |
| bag | [tests.py](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/bag/tests.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/Caligrifyzone/main/bag/tests.py) | ![screenshot](documentation/validation/py-bag-tests.png) | No Errors |
| bag | [urls.py](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/bag/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/Caligrifyzone/main/bag/urls.py) | ![screenshot](documentation/validation/py-bag-urls.png) | No Errors |
| bag | [views.py](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/bag/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/Caligrifyzone/main/bag/views.py) | ![screenshot](documentation/validation/py-bag-views.png) | No Errors |
| caligrifyzone | [settings.py](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/caligrifyzone/settings.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/Caligrifyzone/main/caligrifyzone/settings.py) | ![screenshot](documentation/validation/py-caligrifyzone-settings.png) | No Errors |
| caligrifyzone | [urls.py](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/caligrifyzone/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/Caligrifyzone/main/caligrifyzone/urls.py) | ![screenshot](documentation/validation/py-caligrifyzone-urls.png) | No Errors |
| caligrifyzone | [views.py](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/caligrifyzone/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/Caligrifyzone/main/caligrifyzone/views.py) | ![screenshot](documentation/validation/py-caligrifyzone-views.png) | No Errors |
| checkout | [admin.py](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/checkout/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/Caligrifyzone/main/checkout/admin.py) | ![screenshot](documentation/validation/py-checkout-admin.png) | No Errors |
| checkout | [forms.py](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/checkout/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/Caligrifyzone/main/checkout/forms.py) | ![screenshot](documentation/validation/py-checkout-forms.png) | No Errors |
| checkout | [models.py](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/checkout/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/Caligrifyzone/main/checkout/models.py) | ![screenshot](documentation/validation/py-checkout-models.png) | No Errors |
| checkout | [signals.py](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/checkout/signals.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/Caligrifyzone/main/checkout/signals.py) | ![screenshot](documentation/validation/py-checkout-signals.png) | No Errors |
| checkout | [test_forms.py](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/checkout/test_forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/Caligrifyzone/main/checkout/test_forms.py) | ![screenshot](documentation/validation/py-checkout-test_forms.png) | No Errors |
| checkout | [test_models.py](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/checkout/test_models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/Caligrifyzone/main/checkout/test_models.py) | ![screenshot](documentation/validation/py-checkout-test_models.png) | No Errors |
| checkout | [test_signals.py](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/checkout/test_signals.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/Caligrifyzone/main/checkout/test_signals.py) | ![screenshot](documentation/validation/py-checkout-test_signals.png) | No Errors |
| checkout | [test_views.py](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/checkout/test_views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/Caligrifyzone/main/checkout/test_views.py) | ![screenshot](documentation/validation/py-checkout-test_views.png) | No Errors |
| checkout | [tests.py](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/checkout/tests.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/Caligrifyzone/main/checkout/tests.py) | ![screenshot](documentation/validation/py-checkout-tests.png) | No Errors |
| checkout | [urls.py](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/checkout/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/Caligrifyzone/main/checkout/urls.py) | ![screenshot](documentation/validation/py-checkout-urls.png) | No Errors |
| checkout | [views.py](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/checkout/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/Caligrifyzone/main/checkout/views.py) | ![screenshot](documentation/validation/py-checkout-views.png) | No Errors |
| checkout | [webhook_handler.py](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/checkout/webhook_handler.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/Caligrifyzone/main/checkout/webhook_handler.py) | ![screenshot](documentation/validation/py-checkout-webhook_handler.png) | No Errors |
| checkout | [webhooks.py](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/checkout/webhooks.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/Caligrifyzone/main/checkout/webhooks.py) | ![screenshot](documentation/validation/py-checkout-webhooks.png) | No Errors |
| home | [admin.py](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/home/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/Caligrifyzone/main/home/admin.py) | ![screenshot](documentation/validation/py-home-admin.png) | No Errors |
| home | [models.py](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/home/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/Caligrifyzone/main/home/models.py) | ![screenshot](documentation/validation/py-home-models.png) | No Errors |
| home | [test_views.py](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/home/test_views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/Caligrifyzone/main/home/test_views.py) | ![screenshot](documentation/validation/py-home-test_views.png) | No Errors |
| home | [tests.py](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/home/tests.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/Caligrifyzone/main/home/tests.py) | ![screenshot](documentation/validation/py-home-tests.png) | No Errors |
| home | [urls.py](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/home/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/Caligrifyzone/main/home/urls.py) | ![screenshot](documentation/validation/py-home-urls.png) | No Errors |
| home | [views.py](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/home/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/Caligrifyzone/main/home/views.py) | ![screenshot](documentation/validation/py-home-views.png) | No Errors |
|  | [manage.py](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/manage.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/Caligrifyzone/main/manage.py) | ![screenshot](documentation/validation/py--manage.png) | No Errors |
| products | [admin.py](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/products/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/Caligrifyzone/main/products/admin.py) | ![screenshot](documentation/validation/py-products-admin.png) | No Errors |
| products | [forms.py](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/products/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/Caligrifyzone/main/products/forms.py) | ![screenshot](documentation/validation/py-products-forms.png) | No Errors |
| products | [models.py](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/products/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/Caligrifyzone/main/products/models.py) | ![screenshot](documentation/validation/py-products-models.png) | No Errors |
| products | [test_forms.py](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/products/test_forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/Caligrifyzone/main/products/test_forms.py) | ![screenshot](documentation/validation/py-products-test_forms.png) | No Errors |
| products | [test_models.py](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/products/test_models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/Caligrifyzone/main/products/test_models.py) | ![screenshot](documentation/validation/py-products-test_models.png) | No Errors |
| products | [test_views.py](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/products/test_views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/Caligrifyzone/main/products/test_views.py) | ![screenshot](documentation/validation/py-products-test_views.png) | No Errors |
| products | [tests.py](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/products/tests.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/Caligrifyzone/main/products/tests.py) | ![screenshot](documentation/validation/py-products-tests.png) | No Errors |
| products | [urls.py](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/products/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/Caligrifyzone/main/products/urls.py) | ![screenshot](documentation/validation/py-products-urls.png) | No Errors |
| products | [views.py](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/products/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/Caligrifyzone/main/products/views.py) | ![screenshot](documentation/validation/py-products-views.png) | No Errors |
| products | [widgets.py](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/products/widgets.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/Caligrifyzone/main/products/widgets.py) | ![screenshot](documentation/validation/py-products-widgets.png) | No Errors |
| profiles | [admin.py](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/profiles/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/Caligrifyzone/main/profiles/admin.py) | ![screenshot](documentation/validation/py-profiles-admin.png) | No Errors |
| profiles | [forms.py](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/profiles/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/Caligrifyzone/main/profiles/forms.py) | ![screenshot](documentation/validation/py-profiles-forms.png) | No Errors |
| profiles | [models.py](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/profiles/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/Caligrifyzone/main/profiles/models.py) | ![screenshot](documentation/validation/py-profiles-models.png) | No Errors |
| profiles | [test_forms.py](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/profiles/test_forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/Caligrifyzone/main/profiles/test_forms.py) | ![screenshot](documentation/validation/py-profiles-test_forms.png) | No Errors |
| profiles | [test_views.py](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/profiles/test_views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/Caligrifyzone/main/profiles/test_views.py) | ![screenshot](documentation/validation/py-profiles-test_views.png) | No Errors |
| profiles | [tests.py](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/profiles/tests.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/Caligrifyzone/main/profiles/tests.py) | ![screenshot](documentation/validation/py-profiles-tests.png) | No Errors |
| profiles | [urls.py](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/profiles/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/Caligrifyzone/main/profiles/urls.py) | ![screenshot](documentation/validation/py-profiles-urls.png) | No Errors |
| profiles | [views.py](https://github.com/RadwanDuadu/Caligrifyzone/blob/main/profiles/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/Caligrifyzone/main/profiles/views.py) | ![screenshot](documentation/validation/py-profiles-views.png) | No Errors |


## Responsiveness

I've tested my deployed project to check for responsiveness issues.

| Page | Mobile | Tablet | Desktop | Notes |
| --- | --- | --- | --- | --- |
| Register | ![screenshot](documentation/responsiveness/mobile-register.png) | ![screenshot](documentation/responsiveness/tablet-register.png) | ![screenshot](documentation/responsiveness/desktop-register.png) | Works as expected |
| Login | ![screenshot](documentation/responsiveness/mobile-login.png) | ![screenshot](documentation/responsiveness/tablet-login.png) | ![screenshot](documentation/responsiveness/desktop-login.png) | Works as expected |
| Profile | ![screenshot](documentation/responsiveness/mobile-profile.png) | ![screenshot](documentation/responsiveness/tablet-profile.png) | ![screenshot](documentation/responsiveness/desktop-profile.png) | Works as expected |
| Home | ![screenshot](documentation/responsiveness/mobile-home.png) | ![screenshot](documentation/responsiveness/tablet-home.png) | ![screenshot](documentation/responsiveness/desktop-home.png) | Works as expected |
| Products | ![screenshot](documentation/responsiveness/mobile-products.png) | ![screenshot](documentation/responsiveness/tablet-products.png) | ![screenshot](documentation/responsiveness/desktop-products.png) | Works as expected |
| Product Details | ![screenshot](documentation/responsiveness/mobile-product-details.png) | ![screenshot](documentation/responsiveness/tablet-product-details.png) | ![screenshot](documentation/responsiveness/desktop-product-details.png) | Works as expected |
| Bag | ![screenshot](documentation/responsiveness/mobile-bag.png) | ![screenshot](documentation/responsiveness/tablet-bag.png) | ![screenshot](documentation/responsiveness/desktop-bag.png) | Works as expected |
| Checkout | ![screenshot](documentation/responsiveness/mobile-checkout.png) | ![screenshot](documentation/responsiveness/tablet-checkout.png) | ![screenshot](documentation/responsiveness/desktop-checkout.png) | Works as expected |
| Checkout Success | ![screenshot](documentation/responsiveness/mobile-checkout-success.png) | ![screenshot](documentation/responsiveness/tablet-checkout-success.png) | ![screenshot](documentation/responsiveness/desktop-checkout-success.png) | Works as expected |
| Add Product | ![screenshot](documentation/responsiveness/mobile-add-product.png) | ![screenshot](documentation/responsiveness/tablet-add-product.png) | ![screenshot](documentation/responsiveness/desktop-add-product.png) | Works as expected |
| Edit Product | ![screenshot](documentation/responsiveness/mobile-edit-product.png) | ![screenshot](documentation/responsiveness/tablet-edit-product.png) | ![screenshot](documentation/responsiveness/desktop-edit-product.png) | Works as expected |
| Newsletter | ![screenshot](documentation/responsiveness/mobile-newsletter.png) | ![screenshot](documentation/responsiveness/tablet-newsletter.png) | ![screenshot](documentation/responsiveness/desktop-newsletter.png) | Works as expected |
| FAQs | ![screenshot](documentation/responsiveness/mobile-faq.png) | ![screenshot](documentation/responsiveness/tablet-faq.png) | ![screenshot](documentation/responsiveness/desktop-faq.png) | Works as expected |
| Contact | ![screenshot](documentation/responsiveness/mobile-contact.png) | ![screenshot](documentation/responsiveness/tablet-contact.png) | ![screenshot](documentation/responsiveness/desktop-contact.png) | Works as expected |
| 404 | ![screenshot](documentation/responsiveness/mobile-404.png) | ![screenshot](documentation/responsiveness/tablet-404.png) | ![screenshot](documentation/responsiveness/desktop-404.png) | Works as expected |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Page | Chrome | Firefox | Safari | Notes |
| --- | --- | --- | --- | --- |
| Register | ![screenshot](documentation/browsers/chrome-register.png) | ![screenshot](documentation/browsers/firefox-register.png) | ![screenshot](documentation/browsers/safari-register.png) | Works as expected |
| Login | ![screenshot](documentation/browsers/chrome-login.png) | ![screenshot](documentation/browsers/firefox-login.png) | ![screenshot](documentation/browsers/safari-login.png) | Works as expected |
| Logout| ![screenshot](documentation/browsers/chrome-logout.png) | ![screenshot](documentation/browsers/firefox-logout.png) | ![screenshot](documentation/browsers/safari-logout.png) | Works as expected |
| Profile | ![screenshot](documentation/browsers/chrome-profile.png) | ![screenshot](documentation/browsers/firefox-profile.png) | ![screenshot](documentation/browsers/safari-profile.png) | Works as expected |
| Home | ![screenshot](documentation/browsers/chrome-home.png) | ![screenshot](documentation/browsers/firefox-home.png) | ![screenshot](documentation/browsers/safari-home.png) | Works as expected |
| Products | ![screenshot](documentation/browsers/chrome-products.png) | ![screenshot](documentation/browsers/firefox-products.png) | ![screenshot](documentation/browsers/safari-products.png) | Works as expected |
| Product Details | ![screenshot](documentation/browsers/chrome-product-details.png) | ![screenshot](documentation/browsers/firefox-product-details.png) | ![screenshot](documentation/browsers/safari-product-details.png) | Works as expected |
| Bag | ![screenshot](documentation/browsers/chrome-bag.png) | ![screenshot](documentation/browsers/firefox-bag.png) | ![screenshot](documentation/browsers/safari-bag.png) | Works as expected |
| Checkout | ![screenshot](documentation/browsers/chrome-checkout.png) | ![screenshot](documentation/browsers/firefox-checkout.png) | ![screenshot](documentation/browsers/safari-checkout.png) | Works as expected |
| Checkout Success | ![screenshot](documentation/browsers/chrome-checkout-success.png) | ![screenshot](documentation/browsers/firefox-checkout-success.png) | ![screenshot](documentation/browsers/safari-checkout-success.png) | Works as expected |
| Add Product | ![screenshot](documentation/browsers/chrome-add-product.png) | ![screenshot](documentation/browsers/firefox-add-product.png) | ![screenshot](documentation/browsers/safari-add-product.png) | Works as expected |
| Edit Product | ![screenshot](documentation/browsers/chrome-edit-product.png) | ![screenshot](documentation/browsers/firefox-edit-product.png) | ![screenshot](documentation/browsers/safari-edit-product.png) | Works as expected |
| Newsletter | ![screenshot](documentation/browsers/chrome-newsletter.png) | ![screenshot](documentation/browsers/firefox-newsletter.png) | ![screenshot](documentation/browsers/safari-newsletter.png) | Works as expected |
| Contact | ![screenshot](documentation/browsers/chrome-contact.png) | ![screenshot](documentation/browsers/firefox-contact.png) | ![screenshot](documentation/browsers/safari-contact.png) | Works as expected |
| FAQs | ![screenshot](documentation/browsers/chrome-faq.png) | ![screenshot](documentation/browsers/firefox-faq.png) | ![screenshot](documentation/browsers/safari-faq.png) | Works as expected |
| 404 | ![screenshot](documentation/browsers/chrome-404.png) | ![screenshot](documentation/browsers/firefox-404.png) | ![screenshot](documentation/browsers/safari-404.png) | Works as expected |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues. Some warnings are outside of my control, and mobile results tend to be lower than desktop.

| Page | Mobile | Desktop |
| --- | --- | --- |
| Register | ![screenshot](documentation/lighthouse/mobile-register.png) | ![screenshot](documentation/lighthouse/desktop-register.png) |
| Login | ![screenshot](documentation/lighthouse/mobile-login.png) | ![screenshot](documentation/lighthouse/desktop-login.png) |
| Logout | ![screenshot](documentation/lighthouse/mobile-logout.png) | ![screenshot](documentation/lighthouse/desktop-logout.png) |
| Profile | ![screenshot](documentation/lighthouse/mobile-profile.png) | ![screenshot](documentation/lighthouse/desktop-profile.png) |
| Home | ![screenshot](documentation/lighthouse/mobile-home.png) | ![screenshot](documentation/lighthouse/desktop-home.png) |
| Products | ![screenshot](documentation/lighthouse/mobile-products.png) | ![screenshot](documentation/lighthouse/desktop-products.png) |
| Product Details | ![screenshot](documentation/lighthouse/mobile-product-details.png) | ![screenshot](documentation/lighthouse/desktop-product-details.png) |
| Bag | ![screenshot](documentation/lighthouse/mobile-bag.png) | ![screenshot](documentation/lighthouse/desktop-bag.png) |
| Checkout | ![screenshot](documentation/lighthouse/mobile-checkout.png) | ![screenshot](documentation/lighthouse/desktop-checkout.png) |
| Checkout Success | ![screenshot](documentation/lighthouse/mobile-checkout-success.png) | ![screenshot](documentation/lighthouse/desktop-checkout-success.png) |
| Add Product | ![screenshot](documentation/lighthouse/mobile-add-product.png) | ![screenshot](documentation/lighthouse/desktop-add-product.png) |
| Edit Product | ![screenshot](documentation/lighthouse/mobile-edit-product.png) | ![screenshot](documentation/lighthouse/desktop-edit-product.png) |
| Newsletter | ![screenshot](documentation/lighthouse/mobile-newsletter.png) | ![screenshot](documentation/lighthouse/desktop-newsletter.png) |
| FAQs | ![screenshot](documentation/lighthouse/mobile-faq.png) | ![screenshot](documentation/lighthouse/desktop-faq.png) |
| Contact | ![screenshot](documentation/lighthouse/mobile-contact.png) | ![screenshot](documentation/lighthouse/desktop-contact.png) |
| 404 | ![screenshot](documentation/lighthouse/mobile-404.png) | ![screenshot](documentation/lighthouse/desktop-404.png) |

## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Screenshot |
| --- | --- | --- | --- | --- |
| Products | Feature is expected to allow users to browse products without registration. | Opened product pages as a guest user. | Products were fully accessible without requiring registration. | ![screenshot](documentation/defensive/products.png) |
| | Feature is expected to sort products by price and name. | Tested sorting options for price (low-to-high/high-to-low) and name (alphabetical). | Sorting worked correctly for all options. | ![screenshot](documentation/defensive/sorting.png) |
| | Feature is expected to filter products by category. | Applied category filters while browsing products. | Filters worked as expected, displaying only relevant products. | ![screenshot](documentation/defensive/filtering.png) |
| | Feature is expected to show detailed product information. | Clicked on individual products to view details. | Product details (description, price, image) were displayed correctly. | ![screenshot](documentation/defensive/product-details.png) |
| Shopping Cart | Feature is expected to allow customers to add items to the cart with quantity controls. | Added products to the cart and adjusted quantities. | Items were added successfully, and quantities updated as expected. | ![screenshot](documentation/defensive/add-to-cart.png) |
| | Feature is expected to allow customers to view and manage their cart. | Opened the cart page and edited cart contents. | Cart contents were displayed, updated, and removed correctly. | ![screenshot](documentation/defensive/manage-cart.png) |
| Checkout | Feature is expected to display cart items, grand total, and input fields for checkout. | Proceeded to checkout with items in the cart. | Checkout page displayed cart items, total, and input fields as expected. | ![screenshot](documentation/defensive/checkout.png) |
| | Feature is expected to allow secure payment via Stripe. | Entered valid card details using Stripe at checkout. | Payment was processed securely, and an order confirmation page was displayed. | ![screenshot](documentation/defensive/stripe-payment.png) |
| | Feature is expected to send a confirmation email after purchase. | Completed a purchase and checked email inbox. | Confirmation email was received with order details. | ![screenshot](documentation/defensive/confirmation-email.png) |
| | Feature is expected to display an order confirmation page with an order number. | Completed a purchase. | Order confirmation page displayed successfully with an order number. | ![screenshot](documentation/defensive/stripe-payment.png) |
| Account Management | Feature is expected to allow returning customers to log in and view past orders. | Logged in as a returning customer and accessed order history. | Past orders were displayed correctly in the account section. | ![screenshot](documentation/defensive/order-history.png) |
| | Feature is expected to remember the shipping address for returning customers. | Completed multiple checkouts as a returning customer. | Shipping address was pre-filled on subsequent purchases. | ![screenshot](documentation/defensive/order-history.png) |
| Admin Features | Feature is expected to allow the site owner to create new products. | Created new products with valid data (name, price, description, image, category). | Products were added successfully and displayed on the site. | ![screenshot](documentation/defensive/create-product.png) |
| | Feature is expected to allow the site owner to update product details. | Edited product details as an admin user. | Product updates were saved and displayed correctly. | ![screenshot](documentation/defensive/update-product.png) |
| | Feature is expected to allow the site owner to delete products. | Deleted a product from the inventory. | Product was removed successfully from the site, after being prompted to confirm first. | ![screenshot](documentation/defensive/delete-product.png) |
| Orders | Feature is expected to allow the site owner to view all orders placed. | Accessed the orders dashboard as an admin user. | All orders were displayed correctly. | ![screenshot](documentation/defensive/view-orders.png) |
| Newsletter | Feature is expected to allow users to sign up for the newsletter. | Submitted valid email addresses for newsletter registration. | Email addresses were successfully added to the newsletter list. | ![screenshot](documentation/defensive/newsletter.png) |
| Contact | Feature is expected to allow users to learn more about the website and a form that allows to contact the website owner. | Submitted valid form submission to add new message that a contact request was submitted. | contact model and database is incrememnted on submission of contact form. | ![screenshot](documentation/defensive/contact.png) |
| FAQs | Feature is expected to allow users to learn more about the most commonly asked questions | Page displays a list of most common questions | Page is displaying the most popular questions | ![screenshot](documentation/defensive/faq.png) |
| 404 Error Page | Feature is expected to display a 404 error page for non-existent pages. | Navigated to an invalid URL (e.g., `/test`). | A custom 404 error page was displayed as expected. | ![screenshot](documentation/defensive/404.png) |

## User Story Testing

| Target | Expectation | Outcome | Screenshot |
| --- | --- | --- | --- |
| As a guest user | I would like to browse products without needing to register | so that I can shop freely before deciding to create an account. | ![screenshot](documentation/features/product-list.png) |
| As a guest user | I would like to be prompted to create an account or log in at checkout | so that I can complete my purchase and track my order history. | ![screenshot](documentation/features/checkout.png) |
| As a guest user | I would like to be able to register | so that I can save my information and billing information for future purchases | ![screenshot](documentation/features/register.png) |
| As a user | I would like to log into the website | so that I can view previous order history | ![screenshot](documentation/features/login.png) |
| As a user | I would like to logout into the website | so that I can scroll the website as an guest user | ![screenshot](documentation/features/logout.png) |
| As a user | I would like to sign up to the site's newsletter | so that I can stay up to date with any upcoming sales or promotions. | ![screenshot](documentation/features/newsletter.png) |
| As a customer | I would like to browse various product categories (clothing, toys, jewelry, kitchen gadgets, etc.) | so that I can easily find what I'm looking for. | ![screenshot](documentation/defensive/filtering.png) |
| As a customer | I would like to sort products by price (low-to-high/high-to-low) and name (alphabetical) | so that I can quickly organize items in a way that suits my shopping style. | ![screenshot](documentation/defensive/sorting.png) |
| As a customer | I would like to filter products by category | so that I can narrow down the products to the types I am most interested in. | ![screenshot](documentation/defensive/filtering.png) |
| As a customer | I would like to click on individual products to view more details (description, price, image, etc.) | so that I can make an informed decision about my purchase. | ![screenshot](documentation/features/product-details.png) |
| As a customer | I would like to add items to my shopping cart using quantity increment/decrement buttons | so that I can adjust how many units of a product I want before checkout. | ![screenshot](documentation/features/product-details.png) |
| As a customer | I would like to view and manage my shopping cart | so that I can review, add, or remove items before proceeding to checkout. | ![screenshot](documentation/features/bag.png) |
| As a customer | I would like to adjust the quantity of items in my cart | so that I can modify my purchase preferences without leaving the cart. | ![screenshot](documentation/features/bag.png) |
| As a customer | I would like to remove items from my cart | so that I can remove products I no longer wish to buy. | ![screenshot](documentation/features/bag.png) |
| As a customer | I would like to proceed to checkout where I see my cart items, grand total, and input my name, email, shipping address, and card details | so that I can complete my purchase. | ![screenshot](documentation/features/checkout.png) |
| As a customer | I would like to receive a confirmation email after my purchase | so that I can have a record of my transaction and order details. | ![screenshot](documentation/defensive/confirmation-email.png) |
| As a customer | I would like to see an order confirmation page with a checkout order number after completing my purchase | so that I know my order has been successfully placed. | ![screenshot](documentation/features/order-confirmation.png) |
| As a customer | I would like to securely enter my card details using Stripe at checkout | so that I can feel confident my payment information is protected. | ![screenshot](documentation/features/checkout.png) |
| As a returning customer | I would like to be able to log in and view my past orders | so that I can track my previous purchases and order history. | ![screenshot](documentation/defensive/order-history.png) |
| As a returning customer | I would like the checkout process to remember my shipping address | so that future purchases are quicker and easier. | ![screenshot](documentation/features/checkout.png) |
| As a site owner | I would like to create new products with a name, description, price, images, and category | so that I can add additional items to the store inventory. | ![screenshot](documentation/features/product-add.png) |
| As a site owner | I would like to update product details (name, price, description, image, category) at any time | so that I can keep my product listings accurate and up to date. | ![screenshot](documentation/features/product-edit.png) |
| As a site owner | I would like to delete products that are no longer available or relevant | so that I can maintain a clean and accurate inventory. | ![screenshot](documentation/defensive/delete-product.png) |
| As a site owner | I would like to view all orders placed on the website | so that I can track and manage customer purchases. | ![screenshot](documentation/defensive/view-orders.png) |
| As a site owner | I would like to manage product categories | so that I can ensure items are correctly organized and easy for customers to find. | ![screenshot](documentation/defensive/filtering.png) |
| As a user | I would like to see a FAQ page | See most commonly asked questions | ![screenshot](documentation/features/faqs.png) |
| As a user | I would like to see a 404 error page if I get lost | so that it's obvious that I've stumbled upon a page that doesn't exist. | ![screenshot](documentation/features/404.png) |

## Automated Testing

I have conducted a series of automated tests on my application.

> [!NOTE]  
> I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive.

### Python (Unit Testing)


I have used Django's built-in unit testing framework to test the application functionality. In order to run the tests, I ran the following command in the terminal each time:

- `python3 manage.py test name-of-app`

To create the coverage report, I would then run the following commands:

- `pip3 install coverage`
- `pip3 freeze --local > requirements.txt`
- `coverage run --omit="*/site-packages/*,*/migrations/*,*/__init__.py,env.py,.env" manage.py test`
- `coverage report`

To see the HTML version of the reports, and find out whether some pieces of code were missing, I ran the following commands:

- `coverage html`
- `python3 -m http.server`

Below are the results from the full coverage report on my application that I've tested:

![screenshot](documentation/automation/html-coverage.png)

#### Unit Test Issues

## Bug

### Fixed Bugs

[![GitHub issue custom search](https://img.shields.io/github/issues-search/RadwanDuadu/Caligrifyzone?query=is%3Aissue%20is%3Aclosed%20label%3Abug&label=Fixed%20Bugs&color=green)](https://www.github.com/RadwanDuadu/Caligrifyzone/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)

I've used [GitHub Issues](https://www.github.com/RadwanDuadu/Caligrifyzone/issues) to track and manage bugs and issues during the development stages of my project.

All previously closed/fixed bugs can be tracked [here](https://www.github.com/RadwanDuadu/Caligrifyzone/issues?q=is%3Aissue+is%3Aclosed+label%3Abug).

![screenshot](documentation/bugs/gh-issues-closed.png)

### Unfixed Bugs

[![GitHub issue custom search](https://img.shields.io/github/issues-search/RadwanDuadu/Caligrifyzone?query=is%3Aissue%2Bis%3Aopen%2Blabel%3Abug&label=Unfixed%20Bugs&color=red)](https://www.github.com/RadwanDuadu/Caligrifyzone/issues?q=is%3Aissue+is%3Aopen+label%3Abug)

Any remaining open issues can be tracked [here](https://www.github.com/RadwanDuadu/Caligrifyzone/issues?q=is%3Aissue+is%3Aopen+label%3Abug).

![screenshot](documentation/bugs/gh-issues-open.png)

### Known Issues

| Issue | Screenshot |
| --- | --- |
| The project is designed to be responsive from `375px` and upwards, in line with the material taught on the course LMS. Minor layout inconsistencies may occur on extra-wide (e.g. 4k/8k monitors), or smart-display devices (e.g. Nest Hub, Smart Watches, Gameboy Color, etc.), as these resolutions are outside the project’s scope, as taught by Code Institute. | ![screenshot](documentation/issues/poor-responsiveness.png) |
| With a known order-number, users can brute-force "checkout_success.html" and see potentially sensitive information. | ![screenshot](documentation/issues/stripe-payment.png) |


> [!IMPORTANT]  
> There are no remaining bugs that I am aware of, though, even after thorough testing, I cannot rule out the possibility.
<img src="https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/Guitar-Vault_banner.png">

*Disclaimer: This site has been developed for educational purposes only and forms the final project for assessment through the Code Institute Full Stack Software Developer diploma.* 

<br/>

***
<img src="https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/GV-Logo.png" align="left" width="100px">
<h1 align="center"> Welcome to the Guitar Vault! </h1>
<h4 align="center"> A subscription service for guitarists</h4>
<h4 align="center"> Keep your G.A.S.* turned down and your amp turned up! </h4>
<p align="center"><sup><i>*G.A.S. Gear Acquisition Syndrome - affects many guitarists with an all consuming desire to expand your collection of gear</i></sup></p> 
<p align="center">Link to deployed site: https://guitar-vault.herokuapp.com/</p>
<h1 align="center" height="100" width="100">:guitar: :notes: :metal:</h1>
<br clear="left"/>

***

# CONTENTS

- [OVERVIEW](#overview) 
- [USER EXPERIENCE (UX)](#user-experience-ux)
- [STRATEGY](#strategy)
    - [BUSINESS STRATEGY](#business-strategy)
    - [USER STORIES](#user-stories)
    
- [SCOPE](#scope)

- [STRUCTURE](#structure)

- [SKELETON](#skeleton)
    - [WIREFRAMES](#wireframes)

- [SURFACE](#surface)
    - [INFLUENCES](#influences)
    - [KEY ELEMENT STYLES](#key-element-styles)

- [FEATURES](#features)
    - [PLANNED FEATURES](#planned-features)
    - [FUTURE ENHANCEMENTS](#future-enhancements)

- [TESTING](#testing)

- [BUGS](#bugs)
    - [LIVE](#live)
    - [FIXED](#fixed)

- [DEPLOYMENT](#deployment)

- [TECHNOLOGIES](#technologies)

- [ACKNOWLEDGEMENTS](#acknowledgements)
    - [CODING SUPPORT](#coding-support)
    - [IMAGES](#images)

***

# OVERVIEW
The site offers a subscription service for guitarist. Members enjoy access to a range of guitars (electric, acoustic and bass). Tiered subscription plans provide access to higher value instruments as well as provision of additional services (including express delivery and full guitar set-up). Members receive a 'plectrum' in exchange for their subscription fee which is used to grab a :guitar: from the vault. 

Guitar Vault has been built using <img valign="middle" height="50" src="https://github.com/devicons/devicon/blob/master/icons/django/django-original.svg"/> a <img valign="middle" height="40" src="https://github.com/devicons/devicon/blob/master/icons/python/python-original-wordmark.svg"/> framework, and also employs <img valign="middle" height="40" src="https://github.com/devicons/devicon/blob/master/icons/html5/html5-plain-wordmark.svg"/> <img valign="middle" height="40" src="https://github.com/devicons/devicon/blob/master/icons/css3/css3-plain-wordmark.svg"/> <img valign="middle" height="30"  src="https://github.com/devicons/devicon/blob/master/icons/javascript/javascript-plain.svg"/> and <img valign="middle" height="35" src="https://github.com/devicons/devicon/blob/master/icons/jquery/jquery-plain-wordmark.svg"/>. The deployed site is hosted on <img valign="middle" height="40" src="https://github.com/devicons/devicon/blob/master/icons/heroku/heroku-original-wordmark.svg"/>, the static and media images are hosted in the :cloud:  with <img valign="middle" height="75" src="https://github.com/devicons/devicon/blob/master/icons/amazonwebservices/amazonwebservices-plain-wordmark.svg"/>, whilst payments are processed through <img valign="middle" src="https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/cc-stripe.png"/>. A fully responsive site layout is handled through <img valign="middle" height="40" src="https://github.com/devicons/devicon/blob/master/icons/bootstrap/bootstrap-plain-wordmark.svg"/>.

Many guitarists suffer from G.A.S. (Gear Acquisition Syndrome) - a desire to accrue a range of guitars (as well as amps and pedals) to expand their tonal possibilities. There are many downsides to this, principally the bank balance battering and the need for space for all these instruments. And of course, you can only play 1 guitar at a time. Often the G.A.S. niggle is only temporarily quelled with a new purchase, before the urge for the next guitar takes over! This is where Guitar Vault comes in. Through this service, members get the chance to get their hands on a high end instrument and although these will only be in your possession for a month, the remedy comes from another guitar of your choosing to keep your playing rocking on and G.A.S. levels tuned down!    

------
# USER EXPERIENCE (UX)
## STRATEGY

### BUSINESS STRATEGY

The business goals of Guitar Vault are;
- generate income through a paid subscription service
- provide clear images and information on the available guitars to entice new clients & retain existing clients
- have a clear and simple business proposition

### USER STORIES

| As a...         | I want to...                       | Because...                                               |
|-----------------|------------------------------------|----------------------------------------------------------|
| site user (any) | Understand the purpose of the site | See if this is relevant to me                            |
| site user (any) | Easily navigate the site           | Find the content I'm looking for                         |
| site user (any) | Be able to view the site on any size screen | So all content / images can be seen clearly     |
| site user (any) | Have clear information on pricing  | To decide if to join / which plan is affordable          |
| site user (any) | Be able to filter / search guitars | To find guitars which match my interests                 |
| site user (any) | Be able to see detailed information about the guitars | Match instruments with my preferences |
| site user (any) | Register for an account            | To become a member                                       |
| registered user | Pay for my subscription plan easily| Clarity if / how much I have been charged                |
| registered user | Login / out easily                 | Access / exit my account                                 |
| registered user | Be able to recover/reset my password | Access my account                                      |
| registered user | Be able to manage my subscription  | Change / cancel my subscription plan                     |
| registered user | Select a guitar to receive         | To obtain the guitar                                     |
| registered user | Save particular guitars as favourites| For future choices                                     |
| registered user | See a list of the guitars I've had with my rating| For future choices                         |
| registered user | See ratings given by other users   | To inform my decisions                                   |
| site administrator | View and manage guitars         | Ensuring items are available to view / loan              |
| site administrator | View / manage registered members| Visibility of subscribed members                         |
| site administrator | View / manage subscription plans| Ensure correct prices are displayed / charged            |
| site administrator | View / manage subscription orders| Visibility of members who have signed up                |


------
## SCOPE
The scope of this activity includes;
- provision of a site which satisfies user stories in being able to view, interact through the front-end.
- manage site content (guitars, categories, orders and subscription plans) through custom CRUD forms.
- enable payments to be made and recorded.

Out of scope;
- additional activities which in a real business would be required, such as; scheduling of on-going monthly payments (only the initial payment is demonstrated), inventory management systems relating to the handling / scheduling of guitar loan bookings, delivery & collection processes, etc.

------
## STRUCTURE


### FRONT END STRUCTURE & SCREEN FLOW

The structure of the site should provide a clean and clear interface for site users. Leveraging from django's app structure, there will be specific page content for each app module, yet a baseline html view will be applied consistently across all pages. Site navigation will primarily be through the navigation menu displayed in the header (and through an icon for small screen devices). The only exception to this will be the additional on-screen links (visually displayed as buttons) to proceed to the next / return to the last view (e.g. proceeding to the payment form).
![ScreenFlow](https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/screenflow.png)

### DATABASE STRUCTURE

This build will leverage django's SQLite database during development. Upon deployment this will migrate to POSTGRES (once hosted on HEROKU).

The diagram below outlines the core components of the database - the individual tables, their expected fields and relationships between them. Most tables will be structured within their own django app with some exceptions (e.g. guitars and categories will both be held in the same model).

In summary;
- Categories - classifies guitars (Electric, Bass or Acoustic)
- Guitars - houses all information relating to each guitar including the image ID
- Subscription Plans - contains the tier (Platinum, Gold, Silver and Bronze) their price and details of any additional features
- Member Profiles - users personal information (delivery address, contact details), active subscription plan, guitar rack (guitar which has been requested to loan) and favourites
- Orders - information on subscription plans purchased through the site
- Accounts - model available to admin to manage accounts (e.g. cancel active subscriptions) and award plectrums monthly NOTE: the need for the accounts model was identified during development to seperate ongoing management from the original order and does not feature in the original diagram).

![Planned DB Structure](https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/Planned%20db%20structure.png)

------
## SKELETON
### WIREFRAMES

Wireframes were developed in Adobe XD, png exports are attached below. Initial designs were produced for desktop view with the intention of columns being condensed (via Bootstrap responsive grid). An example mobile screen was produced for the home screen but not for the other html pages.

Homepage (desktop)

![Homepage desktop](https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/Homepage-Desktop.png)


Homepage (mobile)

![Homepage mobile](https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/Homepage-Mobile.png)


Login/Out (desktop)

![Login out](https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/Login_Out.png)


Guitars List View (desktop)

![Guitar List View](https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/GuitarList.png)


Guitar Detail View (desktop)

![Guitar Detail View](https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/GuitarDetail.png)


Sign-Up / Payment (desktop) *note these were split into 2 separate screens in the final development to leverage django allauth for sign-up independently from payments*

![SignUp Payment](https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/Sign-upForm.png)


Members Profile (desktop) *planned but not yet implemented*

![Profile](https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/Profile.png)


## SURFACE
### INFLUENCES
Inspiration for the site layout was taken from on-line music retailers. An example is shown below which has a bootstrap style responsive grid layout.

Example guitar retailer:

![retailer](https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/ExampleRetailer.png)


Inspiration for site logo text:

![logos](https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/Logos.png)

### KEY ELEMENT STYLES

LOGO

The site logo took great influence from the 'serif' style logos of some of the greatest known guitar and amp brands (i.e. Marshall, Gibson and Fender). A font was found which paid homage to these world famous logos, yet remained extremely legible.

The site logo-text was achieved by applying the Google Font 'lobster' font-family over a textured 'rust' background which due to the zoom level actually provides a slight 'aged leather' look. A font mask* was then applied using another 'gold' texture image (both texture images were licensed from Adobe Stock). The layering was achieved in CSS using a combination of text-fill and background-clip with a back-up gold font* (declared in the root variable as was the font-family). 
* *see acknowledgements for reference used for application of font/text masks*

The CSS is shown here;


``` 
    .gold-special-txt {
        color:var(--off-gold); /*- backup font color if text mask fails -*/  
        background: url('/media/gold-texture.jpg');  
        background-size: cover;
        -webkit-text-fill-color: transparent;
        -webkit-background-clip: text;
        -moz-background-clip:text;
        background-clip:text;
        }
``` 

The final result achieved;

![site logo-text](https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/Guitar-Vault_banner.png)

The same styling class is then also applied to the page titles as shown below;

![site text](https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/subscription.png)

The site logo was produced in Adobe Illustrator (achieved by tracing the outer edges of a photo of my own Gibson SG for an outline).

![site logo image](https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/GV-Logo.png)

It was important to use a 'simple' sans-serif font elsewhere on the site, for which another Google Font was used 'Varta'.

![Varta welcome text](https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/welcome.png)

---
Navigation Bar and Menus

The design of the navigation bar employs bootstrap layout to ensure responsive sizing, bootstrap classes / components to create drop-down menus which collapse into an icon for small screen sizes and django template inheritance to aid structure and responsive selections. These are structured across 3 html files;
- base.html - seen on all screens and hosts the logo and logo-text. Links to Account (i.e. sign-in/out, profile), Shopping Bag and Plectrum* are displayed here in larger screens but hidden on smaller devices.
- mobile-nav-items.html - only displayed for smaller screens and allows for the Account / Shopping Bag & Plectrum* items to be displayed on a lower row (increasing the size available in the upper row for logo).
- main-nav-items.html - contains a row of drop-down menus which employ django url filters to narrow the list of guitar items by category (electric/bass/acoustic) and further sub-categories (e.g. tier, left-handed).This menu is collapsed into a single icon for small screens. It also hosts a 'search bar' which looks for text matches against guitar brands and models.

The elements are styled using the logo fonts 'lobster', standard font 'Varta' and color schemes described elsewhere in this section. Additional custom classes are applied in some cases to override bootstrap defaults (e.g. link styles) and / or size, color and hover state effects. 

*Plectrum is the planned internal 'currency' to loan a guitar which forms part of the member profile not yet implemented.

Navigation Bar - Desktops

![Nav desktop](https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/Nav-desktop.png)

Navigation Bar - Mobile

![Nav mobile](https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/Nav-mobile.png)

---
Buttons 

The site buttons use the Bootstrap classes to determine sizing. Custom classes were applied to apply the colors, including hover states.

An example of the primary button css styling is;

``` 
    .btn-gold-outline {
        color:var(--off-gold);
        border: 3px solid var(--off-gold);
        background-color: var(--transp); /* prevents default white background */
        }
        
    .btn-gold-outline:hover {
        background-color:var(--off-gold);
        color:var(--off-black);
        }
``` 

Button Pre and Post hover

![button](https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/Button.png) ![button-hover](https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/Button-hover.png)

---
Guitar Cards

![guitar card](https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/guitarcard.png)

Guitars are displayed using the Bootstrap card class. Combination of django loop and if statements enable a card to be produced for each card which satisfies the filtered view (i.e. all or selective depending on the url view generated). The core components of the card are;

- parent card element - Bootstrap .card class for a responsive card layout which handles margin and padding settings
- image - embedded url links through to the individual card-detail page (which shows additional information)
- .card-overlay & tier pendant - the card overlay acts as a container to position the tier outside of the card-body. The tier pendant combines Font Awesome icon and text label relating to the specific tier of the guitar (*see Tier Pendant section below for more information on the structure of this element*)
- .card-body - container for `<div>`'s which holds flex-box rows (using Bootstrap .d-flex & .flex-row classes) which each hold a pair of `<p>` tags for a label and value with the latter populated through the django loop and template tags.
- .card-footer - container for Add / Remove Favourite and Add / Remove to member's rack icons - note that these form aspect of the members functionality which have not yet been implemented (*see svg section below for more information on the icons*)

Additionally, the cards are held in parent Bootstrap columns so as layout provides a single card (100% screen width) for small screens, increasing through the Bootstrap breakpoints up to 4 cards for extra large screens.
    
<details>
    <summary>Show HTML Extract of card</summary>

    ``` 
           <div class="row">
                    
                    {% for guitar in guitars %}

                        <div class="col-12 col-md-6 col-lg-4 col-xl-3 mb-4">
                            <div class="card bg-dark guitar-card gold-accent-outline">

                                <!--card image -->
                                {% if guitar.image_id %}
                                <a href="{% url 'guitar_detail' guitar.id %}" class="guitar-image-link">
                                    <img src="{{ guitar.image_id.url }}" class="card-img-top" alt="{{ guitar.brand }} {{ guitar.guitar_model }}">
                                </a>

                                {% else %}
                                <a href="{% url 'guitar_detail' guitar.id %}" class="guitar-image-link">
                                    <img src="{{ MEDIA_URL }}noimage.png" class="card-img-top " alt="{{ guitar.brand }} {{ guitar.guitar_model }}">
                                </a>
                                {% endif %}

                                <!-- tier pendant (overlays image)-->
                                <div class="card-custom-overlay pt-0">
                                    <div class="fa-layers fa-fw tier-pendant">
                                        {% if guitar.tier %}
                                            {% if guitar.tier == 'Platinum' %}
                                                <i class="fas fa-bookmark fa-6x tp-platinum"></i>
                                                <!--Longer tier requires different transform adjustments for Platinum -->
                                                <span class="fa-layers-text fa-inverse tp-text" data-fa-transform="rotate--270 right-27">{{ guitar.tier }}</span>
                                            {% else %}    
                                                {% if guitar.tier == 'Gold' %}
                                                    <i class="fas fa-bookmark fa-6x tp-gold"></i>
                                                    
                                                {% elif guitar.tier == 'Silver'%}
                                                    <i class="fas fa-bookmark fa-6x tp-silver"></i>
                                                
                                                {% elif guitar.tier == 'Bronze'%}
                                                    <i class="fas fa-bookmark fa-6x tp-bronze"></i>
                                                
                                                {% endif %}
                                                <span class="fa-layers-text fa-inverse tp-text" data-fa-transform="rotate--270 right-27 up-7">{{ guitar.tier }}</span>
                                            {% endif %}
                                        {% endif %}
                                    </div>
                                </div>

                                <!-- card content -->
                                <h5 class="card-title text-center pt-2">{{ guitar.brand }} - {{ guitar.guitar_model }}</h5>
                                <div class="row card-body">
                                    <div class="col">
                                        <div class="guitar-card-list">
                                            <div class="d-flex flex-row">
                                                <p class="col-6">Category</p>
                                                <p class="col-6">{{ guitar.category }}</p>
                                            </div>
                                            <div class="d-flex flex-row">
                                                <p class="col-6">Status</p>
                                                <p class="col-6">{{ guitar.status }}</p>
                                            </div>
                                            <div class="d-flex flex-row">
                                                <p class="col-6">Handed</p>
                                                <p class="col-6">{{ guitar.handed }}</p>
                                            </div>
                                            <div class="d-flex flex-row">
                                                <p class="col-6">Condition</p>
                                                <p class="col-6">{{ guitar.condition }}</p>
                                            </div>
                                            <div class="d-flex flex-row">
                                                <p class="col-6">Condition Rating</p>
                                                <p class="col-6">{{ guitar.rating_condition }}</p>
                                            </div>
                                            <div class="d-flex flex-row">
                                                <p class="col-6">Overall Rating</p>
                                                <p class="col-6">{{ guitar.rating_overall }}</p>
                                            </div>
                                        </div>
                                    </div>    
                                </div> <!--close card body -->
                                
                                <!--card footer-->
                                <div class="card-footer text-muted">
                                    <ul class="list-inline list-unstyled d-flex justify-content-evenly align-items-baseline">
                                        <li class="list-inline-item w-20 pb-0 ">
                                                                                      
                                            <!--option A : Add Favourite -->
                                            <btn type="button" class="btn btn-sm btn-add-fav align-baseline">
                                                <i class="far fa-heart fa-2x"></i>
                                                <p class="pb-0"><small>Add Favourite</small></p>
                                            </btn>
                                            
                                            <!--option B : Remove Favourite -->
                                            <btn type="button" class="btn btn-sm d-none btn-remove-fav align-baseline">
                                                <i class="fas fa-heart fa-2x"></i>
                                                <p class="ps-2"><small>Remove Favourite</small></p>
                                            </btn>
                                        </li>

                                        <li class="list-inline-item w-20 pb-0 align-baseline">
                                            
                                            <!--option A : Add to Rack -->
                                            <btn type="button" class="btn btn-sm btn-take align-baseline">
                                                <img src="{{ MEDIA_URL }}Guitar_gold_add.svg" class="guitar-svg add-gold">
                                                <img src="{{ MEDIA_URL }}Guitar_black_add.svg" class="guitar-svg add-black">
                                                <p class=""><small>Add to Rack</small></p>
                                            </btn>

                                            <!--option B : Remove from Rack -->
                                            <btn type="button" class="btn btn-sm btn-take d-none align-baseline">
                                                <img src="{{ MEDIA_URL }}Guitar_gold_remove.svg" class="guitar-svg add-gold">
                                                <img src="{{ MEDIA_URL }}Guitar_black_remove.svg" class="guitar-svg add-black">
                                                <p class="ps-2"><small>Remove from Rack</small></p>
                                            </btn>
                                        </li>
                                    </ul>
                                </div>      <!--close card footer -->
                            </div>          <!--close card  -->
                        </div>              <!--close card col -->

                    {% endfor %}

                </div>  <!--close sub-parent card row-->
        
    ``` 
    
</details>
    
---
Tier Pendants

![platinum](https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/platinum.png)![gold](https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/gold.png)![Silver](https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/silver.png)![bronze](https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/bronze.png)

The guitar images have an overlaying pendant displaying the tier (i.e. Platinum, Gold, Silver or Bronze). This was achieved by using a Font Awesome "fa-bookmark" icon for the pendant within an `<i>` tag, with a child `<span>` containing the text. To this the following Font Awesome classes are applied;
- "fa-layers" - applied to parent to allow stacking
- "fa-fw" - to aid alignment
- "fa-layers-text" - applied to span to put the text on top 
- "fa-inverse" - (recommendation on Font Awesome site to prevent background color bleed) although subsequent testing indicates these do not have an affect but remain applied 
- "fa-6x" - increase overall size of the icon
- "data-fa-transform" - attribute applied in-line to set the vertical text direction (set to rotate--270). This attribute was also used to fine tune the  horizontal alignment (centered) and the vertical alignment (top) - with a slight variation for the 'Platinum' tier due to the longer text length.

    *Note:  some of these Font Awesome styles have required the additional SVG and JS version of the script file*
``` 
    <script defer src="https://use.fontawesome.com/releases/v5.15.0/js/all.js"></script>
```     
Further custom classes position the parent card-overlay object and apply the font color with additional data-transform properties applied to Platinum for the sizing reasons mentioned above.  

Extract of the html & CSS are available below, note the application of the django template tags which allows the correct pendant to be allocated to the guitar (held within a loop statement not shown in this extract) which enables the specific custom classes to be applied with the variations specified for 'Platinum'
  
<details>
    <summary>Show HTML Extract</summary>

    ``` 
            <!-- tier pendant (overlays image)-->
            <div class="card-custom-overlay pt-0">
                <div class="fa-layers fa-fw tier-pendant">
                    {% if guitar.tier %}
                        {% if guitar.tier == 'Platinum' %}
                            <i class="fas fa-bookmark fa-6x tp-platinum"></i>
                            <!--Longer tier requires different transform adjustments for Platinum -->
                            <span class="fa-layers-text tp-text" data-fa-transform="rotate--270 right-27">{{ guitar.tier }}</span>
                        {% else %}    
                            {% if guitar.tier == 'Gold' %}
                                <i class="fas fa-bookmark fa-6x tp-gold"></i>

                            {% elif guitar.tier == 'Silver'%}
                                <i class="fas fa-bookmark fa-6x tp-silver"></i>

                            {% elif guitar.tier == 'Bronze'%}
                                <i class="fas fa-bookmark fa-6x tp-bronze"></i>

                            {% endif %}
                            <span class="fa-layers-text tp-text" data-fa-transform="rotate--270 right-27 ">{{ guitar.tier }}</span>
                        {% endif %}
                    {% endif %}
                </div>
            </div>
    ``` 
    
</details>
    

<details>
    <summary>Show CSS Extract</summary>
    ```
        
        .tp-text {
        font-weight:900;
        }

        .card-custom-overlay {
        position:absolute;
        top: 5%;
        right: 25%;
        }

        .tp-platinum {
        color: var(--purple);
        transform: translateY(1.5rem) scale(1,1.5);
        }

        .tp-gold {
        color:var(--gold);
        }

        .tp-silver {
        color:var(--silver);
        }

        .tp-bronze {
        color:var(--bronze);
        }

    ``` 
 
</details>
    
---
Responsive SVG Icons

<img valign="middle" height="100" src="https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/Guitar_black_add.svg"/> <img valign="middle" height="80" src="https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/Guitar_gold_add.svg"/> <img valign="middle" height="125" src="https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/Guitar_black_remove.svg"/> <img valign="middle" height="60" src="https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/Guitar_gold_remove.svg"/>


Font Awesome is used for most of the site icons, one exception was for a guitar shaped icon to be used as a visual aid to add / remove guitars from the member's guitar rack. The icon was drawn in Adobe Illustrator (same image created that was used for the logo icon referred to above). 4 versions were then created for an add / remove and a default and hover version. The hover version was required as the same color scheme was used for the button icon that they reside on. So when the inverse hover button styles was applied these would have hidden the icon.
The images were exported from Adobe in svg format to preserve the crispness (initial efforts in png format resulted in pixelated / skewed images across responsive screens despite their small sizing). The icons are sized in REM (3rem) for responsive sizing. Rather than employ JS or custom SVG classes to change the hover affect colors, a simpler approach was to host all 4 images with 'display:none' set on the hover version. The hover class (applied to the parent) then alternates the display attribute to switch the visible icon held in child `<image>` tags.


---
FAVICON

<img valign="middle" src="https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/favicon.ico"/>

The same guitar icon image was adjusted in Adobe Illustrator to replace the add / remove symbols with GV lettering. When converted to .ico format / sizing, the elongated icon (longer than width) resulted in squashed icon to conform to the boxed 32px x 32px favicon sizing. Retaining the ratio resulted in an icon width which was barely visible. For this reason, the icon was rotated for a corner to corner layout with a background color applied to aid appearance. This was then converted from a png format to .ico format via https://image.online-convert.com/convert-to-svg, whilst https://svgontheweb.com/ also served as a useful reference site for svg creation and site inclusion.

FINAL MOCK-UP

![FINAL MOCKUP](https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/smartmockups.jpg)

------
# FEATURES

## PLANNED FEATURES 


| Key Feature                   | Details.                                                          | Delivered              |
|-------------------------------|-------------------------------------------------------------------|------------------------|
| Ability to create an account  | handled by django all-auth                                        |:white_check_mark:      |
| Login / Out                   | handled by django all-auth                                        |:white_check_mark:      |
| Clear site navigation         | nav shown aross screens with collapse for small screens           |:white_check_mark:      |
| Search for guitars            | handled through nav search bar                                    |:white_check_mark:      |
| Filtered views of guitars     | url views embedded in main nav menus                              |:white_check_mark:      |
| Simple and clear layout of guitars | employs bootstrap .card component                            |:white_check_mark:      |
| Detailed view of guitars      | url from card summary through to detailed card view               |:white_check_mark:      |
| Members can favourite guitars | Via icon on guitar card and can also be removed via profile page  |:white_check_mark:      | 
| Members can add guitars to rack | via icon on guitar card                			    |:white_check_mark:      |
| Members can manage their subscription plans | members can request to cancel via profile page      |:white_check_mark:      |
| Members can provide a rating on guitars loaned | De-scoped - moved to future feature              |:heavy_exclamation_mark:|
| Site poll to get members feedback | Descoped - moved to future feature             		    |:heavy_exclamation_mark:|
| Non-registered visitors see feedback on home screen | Applied through JS to switch comments       |:white_check_mark:      |
| Admin can manage / add guitars | Custom Admin panel includes ability to add/edit/delete guitars   |:white_check_mark:      |
| Admin can manage / add orders  | Custom Admin panel includes ability to add/edit/delete orders    |:white_check_mark:      |
| Admin can manage accounts      | Custom Admin panel includes ability to award plectrums and cancel active accounts|:white_check_mark:|
| Admin can manage guitar loan requests | Custom Admin panel includes ability to view requests (further capabilities are out of scope) |:white_check_mark:      |

## FUTURE ENHANCEMENTS

This list summarises features which were de-scoped from this project and could be implemented as future enhancements.

- Provide members with the ability to rate guitars loaned
  (ratings are hard-coded and can be edited but a fully functional rating would require a history of active users and deemed beyond scope for project purposes)

- Provide Admin with;
    - run a member feedback poll (de-scoped from project)
    - award plectrums through a diarised mechanism (functionality has been added to award plectrums to all active accounts, but more complex / date driven functionality is deemed beyond the scope of this project)

In response to additional testing outcomes;

- Consider switching all images to nextgen formats (webP) with fallback for unsupported browsers

 
------
# TESTING

The majority of testing is performed manually during the development of the project. Upon completion of the project, there were a small number of known bugs. Additional testing was also performed across the site. 
A summary of the key call outs from all testing activities is summarised below, with any key outstanding matters also reflected in either the Bugs or Future Enhancement sections. 
Further information for each of the testing activities is available in the collapsible sections below. Note that attempts to run the django site through django-html-validator was unsuccessful (time constraints did not permit further investigation on how to correctly install and use this package). 


<details>
    <summary>User Story Testing</summary>
    
    
In summary, all user stories tests passed (aside from those de-scoped from the original plan - deemed as being beyond the scope of requirement for the project.
    
| As a...         | I want to...                       | Test Review Notes                                        | Pass / Fail. |
|-----------------|------------------------------------|----------------------------------------------------------|--------------|
| site user (any) | Understand the purpose of the site | Information available from the 'About Us' links 	  |:white_check_mark:|
| site user (any) | Easily navigate the site           | Clear and simple navigation of the site with nav menu on all pages| :white_check_mark:|
| site user (any) | Be able to view the site on any size screen | Fully responsive tested across multiple screen sizes| :white_check_mark:     |
| site user (any) | Have clear information on pricing  | Subscription pricing provided up front and visible during payment steps| :white_check_mark: |
| site user (any) | Be able to filter / search guitars | Achieved through search bar and menus with filtered views| :white_check_mark:        |
| site user (any) | Be able to see detailed information about the guitars | Summary information provided in list view with full info in detailed screen |:white_check_mark:|
| site user (any) | Register for an account            | Through join link handled by allauth, new sign-ups captured in admin db| :white_check_mark: |
| registered user | Pay for my subscription plan easily| Clear laid out payments form with test payments handled through stripe| :white_check_mark:|
| registered user | Login / out easily                 | Links visible on all screens and handled through allauth  | :white_check_mark: |
| registered user | Be able to recover/reset my password | Reset / recovery links with email linkage to generate sending of email| :white_check_mark: |
| registered user | Be able to manage my subscription  | Managed via member's profile page.                         |:white_check_mark:|
| registered user | Select a guitar to loan            | Requested via Add to Rack icon                       	    |:white_check_mark:|
| registered user | Save particular guitars as favourites| Added via favourite icon on guitar card and can also be removed via icon on profile page|:white_check_mark:|
| registered user | See ratings given by other users   | A fixed rating is visible, further enhancements would see this be generated by users ratings| :white_check_mark:|
| site administrator | View and manage guitars         | Managed through the custom site_admin.html page (Guitars)  | :white_check_mark: |
| site administrator | View / manage orders            | Managed through the custom site_admin.html page (Orders)   | :white_check_mark: |
| site administrator | View / manage subscriptions     | Managed through the custom site_admin.html page (Accounts) | :white_check_mark: |
| site administrator | View / manage guitar loans      | Requests can be viewed through the custom site_admin.html page (Guitar Requests), further activity is deemed outside scope of project) | :white_check_mark: |
    
</details>

<details>
<summary>Lighthouse Performance</summary>

Four key site pages were run through the Chrome Inspector Lighthouse for assessment (shown below). Desktop faired better than mobile, but both had shortcomings primarily in performance and accessibility. Please see below for details of responsive action taken.

Index - mobile
    
<img src="https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/lh-index-mobile.png" width="500">
    
Index - desktop
    
<img src="https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/lh-index-desktop.png" width="500">

SignIn/Up - mobile
    
<img src="https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/lh-signin-up-mobile.png" width="500">
    
SignIn/Up - desktop
    
<img src="https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/lh-signin-up-desktop.png" width="500">
    
Subscriptions - mobile
    
<img src="https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/lh-subscriptions-mobile.png" width="500">
    
Subscriptions - desktop
    
<img src="https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/lh-subscriptions-desktop.png" width="500">

Guitars - mobile
    
<img src="https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/lh-guitars-mobile.png" width="500"> 

Guitars - desktop
    
<img src="https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/lh-guitars-desktop.png" width="500">
    
 | Aspect      | Key Causes              | Recommendations (not directly mapped to causes) | Outcome                                 |
 |-------------|-------------------------|---------------------------------------|---------------------------------------------------|
 | Performance | Contentful paint times  | switch png images to next gen formats |  Please see point 1 below                         |
 | Performance | Time to interactivity   | eliminate render blocking resources   |  Causes identified as 3rd party libraries (bootstrap, jquery) outside of my control |                                                 |   
 | Performance | HTTP/1.1                | serve resources over http/2           |  Files identified relate to AWS configuration - lack of knowledge to implement safe changes|
 | Accessibility| Color Contrasts        | Switch colors used                    | This was also self-identified as a possible issue particularly white / gold text with 'gold' coloring scheme for that tier. Some adjustments were made to the background gold to darken from the original selection and also investigated use of text shadows but these were not providing a satisfactory result. Added to future enhancements |
 | Best Practices| Browser errors were logged to the console | Resolve errors     | This was self identified and appears on the outstanding bugs list. The cause is due to JS used to switch feedback which is not displayed if a user is logged in |   
 | SEO          | Links not crawlable | Ensure hrefs link to appropriate destination | At the time of running these reports the 'About US' modals were incomplete but plan to be resolved by the time of project submission |
    
  1. Thorough review undertaken on the guidance to switch jpeg / png images to next gen formats. Steps taken;
        - downloaded Google's Photoshop plugin to convert images to webP (format not natively supported by Adobe)
        - converted the banner background image which reduced the file size by c.50%
        - within the development environment swapped out the jpeg for webP version, re-running the index page for mobiles saw the score improve from 64% to 80%.
        - at this point I was considering adopting this format for all images, however according to caniuse.com not all browsers support - chiefly Safari (only partial support for certain Op Sys).
        - this would mean providing a fall back solution to provide both formats. The task would therefore involve;
        - creating a webP version of all site images
        - saving these to AWS S3 bucket
        - switching existing image tags to a picture with source tags to serve webP or fallback
        - updating the fixture files to have 2 versions of each image (as image links are often not hard-coded but identified via the django loop / tags
        - identifying a fall-back approach where images are served as background-images from the css file.
    For these reasons, the time remaining and the risk of causing unintended behaviours so close to project submission the activity was not progressed but has been added as a future enhancement.
    
</details>


<details>
    <summary>HTML Validation</summary>
Individual HTML pages were run through https://validator.w3.org/. The only errors identified (c. 30 for each page) were all identified as 'parse errors'. These seem to relate to the validators inability to recognise / handle django html templates. All tags were removed in a couple of pages and no other errors were identified providing comfort that there are no concerns with the html structure.
    
</details>


<details>
    <summary>CSS Validation</summary>
    
Prior to validation, the CSS was run through https://autoprefixer.github.io/ to review and apply additional browser compatability extensions. This was then passed through W3C CSS validator and passed with no errors identified. There were 40 warnings identified but upon review these mainly related to the vendor pre-fixes and were of no concern.
    
<img src="https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/w3c_css_validation.png" width="500">    
    

</details>



<details>
    <summary>JS Validation</summary>
Only a small amount of custom JS resides in the construction, there were only 4 issues identified when run through JShint relating to missing semi-colons which have been resolved. 
</details>


<details>
    <summary>Python PEP8 Compliance</summary>
A singificant number of PEP8 compliance issues were identified in the python-linter within the development environment. All reasons for the alerts were reviewed and all were resolved where relating to;

- long line lengths
- trailing white space
- missing blank line at end of code
- missing double row between class blocks
- over / under-indentation
- over / under use of space prior to comment
- items imported but not used	
- use of Null=True on CharFields	

A further 139 remain which were reviewed but not resolved as;
	
- 120 relate to migration files (ignored)
- 15 relate to files not visible in workspace (14 - VS Code, 1 custom_storages.py)
- 4 relate to line lenths in settings.py which investigations suggest to leave as unconfirmed method to split lines
</details>

<details>
    <summary>Responsiveness</summary>
During development, significant checking for responsiveness was performed via Google Inspector. This allowed breakpoint corrections, media queries to be developed at the time of content creation.
    
Post deployment, the site was viewed through lambdatest.com for a selection of screen sizes, browsers and operating systems. Free account limits to 6 tests so a mix of broadening the possible ranges were chosen. The configurations checked are shown in the table below. There was 1 instance of unexpected behaviour encountered affecting Apple devices running iOS (whereby the nav banner 'scrolled' as content below the nav was navigated. However I also checked this manually on an iPhone (X) and Ipad (2019 Pro) and neither of these experienced the same issue. The CSS was also checked and confirmed as having a fixed position. 
    
The CSS was also run through auto-prefixer (as referenced under CSS validation) to ensure any additional vendor pre-fixers were applied.
    
Table of responsive configurations checked;
    
 | Browser      | Device                   | OS        | Resolution | Outcome          |
 |--------------|--------------------------|-----------|------------|------------------|
 |Firefox       |  Mobile - samsung        | Android   | N/A        |:white_check_mark:|
 |Chrome        |  Mobile - Google Pixel 4A| N/A       | N/A        |:white_check_mark:|
 |Safari        |  Mobile - iPhone 12      | iOS       | N/A        |:heavy_exclamation_mark:|
 |Edge          |  Desktop                 | Windows 10| 1280 x 800 |:white_check_mark:|
 |Chrome        |  Desktop                 | Windows 8.1|1600 x 1200|:white_check_mark:|
 |Safari        |  Desktop                 | macOS Mojave| 1024 x 768|:white_check_mark:|
 
 Note: Tables within the site_admin model (used by administrators to view / manage lists of guitars, orders, accounts and guitar requests) have a media query to reduce font-size on small screens but can on mobile devices still require horizontal scrolling. As it would be unlikely that the business would manage these tasks via a mobile device this has been accepted.

</details>

------
# BUGS
## LIVE

| Item      | Details                              | Additional Notes                                                                    | Current Status    |
|-----------|--------------------------------------|-------------------------------------------------------------------------------------|-------------------|
| Some {{empty}} sections not rendering | Some messages not displaying where there are no values  | In most cases the use of {{empty}} works as intended (e.g. filtering guitars where there are no results, but there are instances (e.g. profile) if a user has not favourited a guitar the <p> message is not displayed  | OPEN | 



## FIXED 
Items fixed post initial deployment

| Item      | Details                              | Additional Notes                        | Current Status                                                |
|-----------|--------------------------------------|-----------------------------------------|---------------------------------------------------------------|
| Image Carousel | Carousel timing issues| Initially planned to have a single carousel which showed multiple images which scrolled across the page. Bootstrap did not seem to support this so multiple carousels were created and timed to scroll, but factors influence the rendering / JS timing impacting the visual experience | FIXED :white_check_mark: Refer to Issues #11 |
| About Us modals | Inconsistent behaviour in deployed vs development environments | The modal content is held in a block on the base template with block tags on the main-nav items (where links to the modals reside) as well as index.html as there are also links in the About Us section. These work as planned in development, but deployed site has inconsistent behaviour with either not showing or showing but without CSS being applied. These were late additions to the site without time to investigate a fix or switch to hosting on individual html pages. | FIXED :white_check_mark: Refer to Issues #13 |
| File Naming Conventions | Ensure standards for file naming conventions applied (i.e. no capitalisation for image files) | Identified in initial assessment | FIXED :white_check_mark: Refer to Issues #1 |


------
# DEPLOYMENT

## Pre-Requisites

Accounts will be required with the following service providers. Free accounts can be created, but some may require credit card authentication.

- [GitHub](https://github.com) - to clone the repository
- [Heroku](https://www.heroku.com) - to host the deployed site
- [Stripe](https://dashboard.stripe.com/register) - payment processing
- [AWS](https://aws.amazon.com/) - cloud based storage service for static and media files

## Local Deployment

1. Clone this repository;
    - click Code
    - copy the HTTPS address
    - within your IDE open the GIT BASH terminal
    - navigate to the directory where you wish the cloned directory to be made
    - enter git clone followed by the URL copied earlier:
    ```
    git clone https://github.com/KelvenH/Guitar-Vault.git
    ```
    - a clone of the repository will now be created
  
2. Create local variables 
    note that you will need to create your own local variables either within an env.py file or for example set in Git Workspace applicable to your new development version of the repository for the following. These will also need to be added to Heroku as 'config vars' to enable deployment. 
    
    IMPORTANT: DO NOT INCLUDE THESE PASSWORDS / KEYS WITHIN YOUR GIT FILES (E.G. SETTINGS.PY) OR THEY WILL BE EXPOSED PUBLIClY - EXPOSING YOUR SITE / CONNECTED SERVICES AND IN SOME CASES (SUCH AS AWS) CAN LEAD TO MALICIOUS USE BEING CHARGED TO YOUR REGISTERED CREDIT CARD. 
    The only exception to the above is by including them within an env.py file which is listed in a .gitignore file to prevent them being included in your commits.
    
        Variables;
        -  DEVELOPMENT = TRUE (will enable debug to be set to TRUE to see django error messages which are not visible in the deployed version)
        -  SECRET_KEY - recommend using an online django compliant password generator
        -  STRIPE_PUBLIC_KEY - located by logging into Stripe > Dashboard > Developers tab > API Keys
        -  STRIPE_SECRET_KEY - see Stripe comment above
        -  STRIPE_WH_KEY - see Stripe comment to the Developers tab > Webhooks. This can only be generated once a webhook has been created 
        -  AWS_ACCESS_KEY_ID - available from AWS once a user has been created
        -  AWS_SECRET_ACCESS_KEY - see AWS comment above
        -  DATABASE_URL - generated in HEROKU (located under Settings > Config Vars) once PostGres SQL has been added
        
3. Install the apps as listed in the requirements.txt file, this can achieved by the following git command:
    ```
        pip3 install requirements.txt
    ```
    
4.  Apply database migrations to initiate your database and admin panel structure - if no prior changes have been made you should be able to run the final command, but the previous 3 commands are recommended and will be required if changes have been made to the models prior to migration (and repeated after subsequent changes are made):
    ```
        python3 manage.py makemigrations --dry-run
        python3 manage.py makemigrations 
        python3 manage.py migrate --plan
        python3 manage.py migrate
    ```
    
5.   Create a superuser account to be able to access admin and log-in to your local version of the site (provides allauth permissions):
   
   ```
        python3 manage.py create superuser
   ```
   
6. You will be able to run the site on a local host by running the command:

   ```
        python3 manage.py runserver
   ```

7. After exposing port 8000 when prompted or via the git remote explorer panel you will be able to access the site
8. Adding /admin to the home url will present you with the admin panel - you will need to enter the credentials used in step 5 to create the superuser

## Heroku Deployment

1. Log in to [Heroku]((https://www.heroku.com))
2. Go to New > Create New App
3. Provide a name and select your local region 
4. Once in your app, go to Resources > Add Ons and enter PostGres within the input field (selecting the free version)
5. Return to your IDE and within the CLI install the following packages (dj_database_url enables configuration with Heroku hosted database whilst psycopg2 is a database adapter:
    ```
        pip3 install dj_database_url
        pip3 install psycopg2-binary
        pip3 freeze > requirements.txt
    ```
6. Re-run migrations (all 4 commands shown in step 4) to connect to the new Heroku database
7. Import the data held in fixture files (in the shown order):
     ```
        python3 manage.py loaddata categories
        python3 manage.py loaddata guitars
        python3 manage.py loaddata subscriptions
    ```
 
 8. Create a new superuser account for the Heroku database / admin:
    ```
        python3 manage.py createsuperuser
    ```
 
 9. install gunicorn to handle the wsgi connection:
    ```
        pip3 install gunicorn
    ```
 
 10. Create a Procfile in your repo root directory (or update if the original still exists) to ensure that the web: gunicorn address mirrors the name of your Heroku app for example:
  ```
        web: gunicorn guitr-vault.wsgi:application
  ```
 
 11. Freeze the requirements.txt file to add this app (per the command shown against step 5
    
 12. Log into Heroku via the CLI using the command below - note this requires you actual Heroku credentials and not the super user created in step 8   
   ```
        heroku login -i
   ```
   
 13. Temporarily disable the static files being sent to Heroku:
   ```
        heroku config:set DISABLE_COLLECTSTATIC=1 --app [your Heroku app name here]
   ```

 14. Update settings.py 'Allowed Hosts' to the name of your app (likely located around line 20):
   ```
        ALLOWED_HOSTS = ['your Heroku app name.herokuapp.com', 'localhost']
   ```

 15. Return to Heroku > your app > Deploy and scroll down to Deployment Method and choose GitHub. Then under App Connected to GitHub enter your git username/git repo name and search for your Git repo. Click Connect - you can either opt to push updates manually or (recommended) select the Automatic Deploys.    
 16. Return to your CLI and commit / push to git. If you enabled automatic deployment in Heroku the app will now be built (or do this manually if selected).

 17. The Heroku App Overview tab will indicate that the build is in progress and when this has been completed.
 18. Upon build, click on the Open App icon (top left) to view the live deployed site.
 19. Note that as the static files were disabled you will only be able to view content unstyled (e.g. as CSS forms part of the static content). This will be available after completion of the AWS deployment.
   
   ```
        git add .
        git commit -m "your commit message here"
        git push
   ```
    
20. Create a secret key (either of your choosing or via an online django secure password generator) and within Heroku go to Settings > Reveal Config Vars and add:
    ```
        KEY = SECRET_KEY    VALUE = Your password
    ```
    
21. If not undertaken as one of the pre-requisite tasks, add this to your environment variables so that your development environment can connect to your deployed version. Note that the settings.py file will have an empty string value and will look for this in your env settings already. DO NOT ENTER YOUR KEY INTO THE SETTINGS FILE DIRECTLY FOR THE REASONS STATED PREVIOUSLY.

## AWS 
 Amazon Web Services (AWS) is used to host image and static files in cloud storage. Assuming you have or created an AWS account in the pre-requisites;
 1. Log into AWS and go to the Management Console
 2. Through the Services menu search for 'S3'
 3. Create a new bucket giving an appropriate name (recommended use the same as your Heroku app name), select your region and ensure 'Block all public access' is unchecked (you may need to provide additional acknowledgement of this action).
 4. Upon creation, access the bucket and navigate to Properties > Static Web Hosting
 5. Click to Enable / 'Use this bucket to host website' entering default index.html and error.html into the respective fields (these will not be used) and Save.
 6. Go to Permissions > CORS Configuration and paste / save the code below to enable access between Hero and AWS:
    ```
        [
          {
          "AllowedHeaders": [
              "Authorization"
          ],
          "AllowedMethods": [
              "GET"
          ],
          "AllowedOrigins": [
              "*"
          ],
          "ExposeHeaders": []
          }
        ]
    ```
 7. Note / copy the ARN shown on the CORS Configuration page
 8. Go to Bucket Policy > Policy Generator > Policy Type and select S3 Bucket Policy, within the Principal field enter * and Action select 'Get Object'
 9. Paste the ARN value copied in step 7 and select Add Statement > Generate Policy
 10. Copy the JSON Policy Document and paste into the Bucket Policy Editor (accessed at step 8), prior to saving add ``` /* ``` at the end of the "resource value to append to your app name then Save.
 11. Go to Access Control Lists > Public Access and check 'List Objects', Save to grant access to everyone.
 12. Go to Services menu and search for IAM (Identity Access Management) > Groups > Create New Group providing a relevant name (e.g. manage-Guitar-vault)
 13. Click through following screens to Create Group.
 14. From the left panel select Policies > Create Policy > JSON > Import Managed Policy > Filter Policies and search for AmazonS3Full Access then Import
 15. The Create Policy field will now display the imported policy, change the value shown against "Resource" from * with your ARN (noted at step 7) as follows:
    
   ```
        "Resource": [
			                "arn:aws:s3:::your ARN",
			                "arn:aws:s3:::your ARN/*"
            ]
   ```
    
 16. Review Policy > provide name (e,g, guitar-vault-policy) and description (e.g. Access to S3 for guitar-vault static files) > Create Policy
 17. Go to Groups > select the group you created in step 12 > Permissions > Attach Policy > select the policy created in step 17 > Attach Policy
 18. Users > Add User > provide a username (e.g. guitar-vault-staticfiles-user) > check 'Programmatic Access' > Next
 19. Check the Group (to add the new user to the group created in step 13) > Next through the following screens > Create User
 20. Download the CSV file - note this must be saved locally as can not be re-generated
 21. Return to your IDE and within the CLI install boto3 and django-storages
   ```
            pip3 install boto3
            pip3 install django-storages
            pip3 freeze > requirements.txt
   ```
 
 22. Go to settings.py and update the AWS_STORAGE_BUCKET_NAME and AWS_S3_REGION_NAME to match your AWS S3 bucket
 23. From the .csv file downloaded after the AWS user creation, add the AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY to your environment vairables (NOT WITHIN THE SETTINGS.PY FILE REASONS PREVIOUSLY STATED). The settings.py file is already configured to look for these as env variables.
 24. Reurn to Heroku config vars and these here alongwith a further 'USE_AWS' set to true which will indicate to the settings.py to use these when deployed to Heroku. Whilst here also delete the temporary config var to disable static files (created in step 13 of the Heroku deployment):
 
   ```
        KEY = AWS_ACCESS_KEY_ID         VALUE = from the .csv file
        KEY = AWS_SECRET_ACCESS_KEY     VALUE = from the .csv file
        KEY = USE_AWS                   VALUE = True
        DISABLE_COLLECTSTATIC = 1       *Delete this variable*
   ```
   
 25. If any changes have been made to the development since the last commit, commit and push these changes, additionally if you have not set Automatic Deployment on Heroku, go to Heroku and manually push the latest updates.
 26.  Return to AWS S3 bucket you should now see your static file. Alongside this create a new media/ file and upload your images.
 27.  Note, if using your own images ensure that the file names cross-match with the filenames per the fixture data set (these can also be viewed by navigating to the deployed Admin panel, selecting the object and seeing the image id.
 28.  The images (alongwith the previously added static / CSS) will now be visible in the deployed site.
 
------
# TECHNOLOGIES

## Design; 
- Adobe XD (UI / UX development stage, including simple database structure)
- Adobe Illustrator (headstock logo)

## Languages, frameworks, libraries and apps;
- GitHub (host repository)
- GitPod / VS Code (development environment)
- django (core framework which integrates the following)*
- HTML5
- CSS3
- Bootstrap5 (html / css styles framework)
- Python
* Additional django / utility apps (referenced in requirements.txt);
	- django-allauth (authentication)
 	- django-countries (enables in form dropdown of country codes - required to validated stripe payments)
 	- pillow (enables use of images)
 	- crispy-forms & crispy-bootstrap5 (enable bootstrap styles in rendering form fields)
 	- django-storages (integrate with deployed database)
 	- gunicorn (wsgi web server integration)
 	- dj-database-url (configuration with Heroku hosted database)
 	- psycopg2-binary (PostgreSQL database adapter)
 	- botocore & boto3 - (configure with AWS services)
- Font Awesome - icons
- Google Fonts - typography

## Deployment
- Heroku (including PostGres SQL for database)
- AWS (media and static image hosting)

## Testing
- Lighthouse
- W3C Markup Validation Service (HTML)
- W3C CSS Validation Service (CSS)
- JSHint (JS)
- PEP8 online (Python)
- autoprefixer (browser compatability extensions)
- lamdatest.com (browser / os compatability, responsiveness testing)

## Miscellaneous
- https://miniwebtool.com/django-secret-key-generator/ : django secret key generator
- https://favicon.io/ : favicon converter (svg image created in Adobe Illustrator into .ico format) 
- https://smartmockups.com/ : generated final web site 'mockup' from deployed link for inclusion in README 

------
# ACKNOWLEDGEMENTS

## Coding Support
- CI template : https://github.com/Code-Institute-Org/gitpod-full-template
- Tim Nelson (Mentor): Assigned for project resubmission to whom I'm extremely grateful for his guidance. 
- Boutique Ado (CI Django walkthrough) : large parts of the project especially structure (django models and views) were based on this exercise.
- Net Ninja (YouTube channel https://www.youtube.com/playlist?list=PL4cUxeGkcC9ib4HsrXEYpQnTOTZE1x0uc) : additional guidance on django structures
- Tutor Support (Sean and Igor) : aided with a couple of challenges I struggled to solve (both were due to incorrect referencing of elements in models) 
- Slack : primarily when encountering django obstacles
- StackOverflow : point of reference for number of coding queries
- https://css-tricks.com/how-to-do-knockout-text/ : logo text font mask
- https://svgontheweb.com/ : guidance on creation and styling of SVGS (referred to for add / remove guitar icons).
- https://docs.djangoproject.com/en/3.2/ : django documentation
- https://getbootstrap.com/docs/5.1/getting-started/introduction/ : Bootstrap 5 docs
- https://bringyourownlaptop.com/ - guidance on UI / UX using Adobe XD

## Images
- Adobe Stock Images - licensed for textured masks applied to navigation header and logo font
- Andertons.com - online guitar retailer, used for most of the guitar images (some were also sourced from the manufacturers web sites) and source of the guitar specifications.
- the guitar Vault headstock logo was self drawn in Adobe Illustrator

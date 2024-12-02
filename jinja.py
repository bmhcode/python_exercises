<!DOCTYPE html>
<html lang="en">

<head>
    <title>My Webpage</title>
</head>

<body>
    <ul id="navigation">
        {% for item in navigation %}
        <li><a href="{{ item.href }}">{{ item.caption }}</a></li>
        {% endfor %}
    </ul>

    <h1>My Webpage</h1>
    {{ a_variable }} {# a comment #}
</body>

</html>

{% ... %} for Statements 
{{ ... }} for Expressions to print to the template output 
{# ... #} for Comments not included in the template output 

{% if variable %}
{% elif othervariable %} 
{% else %}
{% endif %} {# This is a template comment that isn't rendered #}. 
             
{% if user %}
    {% extends "base.html" %}
{% else %} 
    {% extends "signup_base.html" %}
{% endif %}

{% block title %} Coffeehouse home page {% endblock %} 

{% include "footer.html" %}
{% if user %}
    {% extends "base.html" %}
{% else %}
    {% extends "signup_base.html" %}
{% endif %} 

{% if variable is divisibleby 10 %}
    do something
{% endif %}

['a','e','i'] the filter statement 
{{variable|length}} # => 3 

{% if coffee.price is equalto 1.99 %} 
    coffee prices equals 1.99 
{% endif %}

{{ users|selectattr("email", "equalto", "webmaster@coffeehouse.com") }}
{# gets users with email webmaster@coffeehouse.com #}
 
{% if variable is string %}
    Yes, the variable is a string!
{% endif %}

if a variable contains latte 
{{variable|reverse}} # => ettal.

variable = ['a','e','i','o','u']
{{variable|first}} # => a
{{variable|last}}  # => u

variable = ['a','e','i','o','u'] 
{{ variable|join("--) }} # => a--e--i--o--u 
The join filter also supports joining certain attributes of an object  
{{ users|join(', ', attribute='username') }}

{{ users|map (attribute='username')|join(', ') }}). 
{{ titles|map('lower')|join(', ') }} 
applies the lower filter to all the elements in 
titles and then joins the items separated by a comma)
def myfunc(n):
    return len(n)

words = ('apple', 'banana', 'cherry')
lengths = map(myfunc, words)
print(list(lengths)) # => [5, 6, 6]

variable = ['a','e','i','o','u'] 
{{variable|random}} # => a, e, i, o, or u

[1,2,3,4,5] the loop statement with this filter 
{% for var  in variable|reject("odd") %}
    {{var}}
{% endfor %} - where odd is the Jinja test – rejects elements that are odd and thus its output is 2 and 4

{% for var in variable|select("odd") %}
    {{var}}
{% endfor %} ==> output is 1, 3, and 5.

["Capuccino"] the filter statement 
{% for var in variable|slice(4) %}
    {{var}}
{% endfor %} outputs ['C', 'a', 'p'],['u', 'c'],['c', 'i'], ['n', 'o'].

{% for var in variable|slice(4,'FILLER') %}
    {{var}}
{% endfor %} 
outputs: ['C', 'a', 'p'],['u', 'c','FILLER'],['c', 'i','FILLER'], ['n', 'o','FILLER'].

{% for var in variable|batch(4) %}
    {{var}}
{% endfor %} 
outputs ['C', 'a', 'p', 'u'],['c', 'c', 'i', 'n'],['o']
{% for var in variable|slice(4,'FILLER') %}
    {{var}}
{% endfor %} 
outputs: ['C', 'a', 'p', 'u'],['c', 'c', 'i', 'n'],['o','FILLER','FILLER','FILLER'].

['e','u','a','i','o'] the statement 
{{variable|sort}} outputs ['a','e','i','o','u']
{{variable|sort(true)}} outputs ['u','o','i','e','a']
{{variable|sort(attribute='date')}} to sort the elements based on the date attribute

# Dictionaries and Objects

dictsort = {'name':'Downtown','city':'San Diego','state':'CA'} 
{% with newdict=variable|dictsort %} ==> newdict = {'city':'San Diego','name':'Downtown','state':'CA'}
(e.g., variable|dictsort(true)), to use sort by value is value as the second argument 
(e.g., variable|dictsort(false,'value') performs a case insensitive sort by value).

{% for ch in coffeehouses|rejectattr("closedon") %} 
{% for u in users|rejectattr("email", "none") %} 
{% for u in users|selectattr("superuser") %} 
{% for u in users|selectattr("email", "none") %} 

# Dictionary definition
 stores = [
 {'name': 'Downtown', 'street': '385 Main Street', 'city': 'San Diego'},
 {'name': 'Uptown', 'street': '231 Highland Avenue', 'city': 'San Diego'},
 {'name': 'Midtown', 'street': '85 Balboa Street', 'city': 'San Diego'},
 {'name': 'Downtown', 'street': '639 Spring Street', 'city': 'Los Angeles'},
 {'name': 'Midtown', 'street': '1407 Broadway Street', 'city': 'Los Angeles'},
 {'name': 'Downton', 'street': '50 1st Street', 'city': 'San Francisco'},
 ]
 <ul>
    {% for group in stores|groupby('city') %}
    <li>{{ group.grouper }}
        <ul>
            {% for item in group.list %}
                <li>{{ item.name }}: {{ item.street }}</li>
            {% endfor %}
        </ul>
    </li>
    {% endfor %}
 </ul>
 # Output
 Los Angeles
    Downtown: 639 Spring Street
    Midtown: 1407 Broadway Street
 San Diego
    Downtown : 385 Main Street
    Uptown : 231 Highland Avenue
    Midtown : 85 Balboa Street
 San Francisco
    Downtown: 50 1st Street
 # Alternate shortcut syntax, produces same output
 <ul>
    {% for grouper, list in stores|groupby('city') %}
        <li>{{ grouper }}
            <ul>
                {% for item in list %}
                <li>{{ item.name }}: {{ item.street }}</li>
                {% endfor %}
            </ul>
        </li>
    {% endfor %}
 </ul
 
# tojson
{{variable|tojson}}
{{variable|tojson(indent=2)}}

# Strings
variable = 'hello world' 
{{variable|capitalize}} outputs Hello world.
variable = 'latte'
{{variable|list}} generates ['l','a','t','t','e']
variable = 'Hello World'
{{variable|lower}} outputs hello world
{% if variable is lower %}Yes, the variable is lowercase!{% endif %} 

{{ "Django 1.8"|replace("1.8", "1.9") }} outputs Django 1.9
{{"oooh Django!"|replace("o", "",2) }} outputs oh Django!

string.- The string filter makes a string unicode if it isn’t already.

variable = 'hello world' 
{{variable|title}} outputs Hello World

variable = 'Hello World' 
{{variable|upper}} outputs HELLO WORLD
if variable is upper %}Yes, the variable is uppercase!{% endif %}

variable = 'Coffeehouse started as a small store' 
{{variable|wordcount}} outputs 6

# Numbers
variable = -5
{{variable|abs}} outputs 5

if a variable contains 250 the filter statement 
{{variable|filesizeformat}} outputs 250 Bytes

{{variable|float("It didn't work")}} returns "It didn't work" if variable can’t 
be converted to a floating-point number

{{'0b001111'|int(0,2)}} a base 2 number outputs 15.

{{ 33.55|round }} output 34.0
{{ 33.55|round(1,'floor') }} outputs 33.5
{{ 33.55|round|int }} outputs 34

{{ items|sum(attribute='price') }}

{% if variable is divisibleby(5) %}
    Variable is divisible by 5!
{% endif %}

even : The even test checks if a number is even.
odd : The odd test checks if a number is odd

# Spacing and Special Characters
{{variable|center(width="15")}} outputs "     mocha     "

escape or e.- The escape or e filter escapes HTML characters from a value. Specifically 
with the escape filter: < is converted to &lt;,> is converted to &gt;,' (single quote) is 
converted to &#39;," (double quote) is converted to &quot;, and & is converted to &amp.
 •	escaped (Test).- The escaped test checks if a value is escaped.
 •	forceescape.- The forceescape filter escapes HTML characters from a value just 
like the escape filter. The difference between both filters is the forceescape filter is 
applied immediately and returns a new and escaped string. This is useful in the rare 
cases where you need multiple escaping or want to apply other filters to the escaped 
results. Normally, you’ll use the escape filter

{{ "%s and %s"|format("Python", "Django!") }} 
outputs Python and Django!

{{ textvariable|indent(2, true) }} 
the 2 indicates two spaces and true indicates to 
indent the first line

safe.- The safe filter marks a string as not requiring further HTML escaping. When 

<b>Coffee</b>house, the <i>best</i> <span>drinks</span> 
{{variable|striptags}} outputs Coffeehouse, the best drinks.

trim.- The trim filter is used to strip leading and trailing whitespace just like 
Python’s string strip() method.

variable = 'Coffeehouse started as a small store' 
{{variable|truncate(20)}} outputs Coffeehouse ... (default = 255 characters)
{{variable|truncate(20,true)}} outputs Coffeehouse start... 
{{variable|truncate(20,true,"!!!")}} would output !!! instead of an elipsis).

variable = 'Coffeehouse started as a small store'
# By default, the wrapping occurs after 79 characters
# Template definition with wordwrap filter for every 12 characters
{{variable|wordwrap(12)}}
# Output
Coffeehouse
started as a
small store


 Listing 4-22. Django xmlattr filter
 # Variable definition
 {% set stores = [
        {'id':123,'name': 'Downtown', 'street': '385 Main Street', 'city': 'San Diego'},
        {'id':243,'name': 'Uptown', 'street': '231 Highland Avenue', 'city': 'San Diego'},
        {'id':357,'name': 'Midtown', 'street': '85 Balboa Street', 'city': 'San Diego'},
        {'id':478,'name': 'Downtown', 'street': '639 Spring Street', 'city': 'Los Angeles'},
        {'id':529,'name': 'Midtown', 'street': '1407 Broadway Street', 'city': 'Los Angeles'},
        {'id':653,'name': 'Downton', 'street': '50 1st Street', 'city': 'San Francisco'},
 ] %}
 # Template definition
 <ul>
    {% for store in stores %}
        <li {{ {'id':'%d'|format(store.id),'class':'%s'|format(store.city|lower|replace(' ','-')) 
            }|xmlattr }}> {{store.city}} {{store.name}}</li>
    {% endfor %}
 </ul>
 # Output
 <ul>
    <li id="123" class="san-diego"> San Diego Downtown</li>
    <li id="243" class="san-diego"> San Diego Uptown</li>
    <li id="357" class="san-diego"> San Diego Midtown</li>
    <li id="478" class="los-angeles"> Los Angeles Downtown</li>
    <li id="529" class="los-angeles"> Los Angeles Midtown</li>
    <li id="653" class="san-francisco"> San Francisco Downton</li>
 </ul>
 
 {{variable|pprint(true)}}
 
 {% now %} Output 11/09/2024 19:47:45
 {% now "F jS o" %}, {% now "F jS o" as today %}
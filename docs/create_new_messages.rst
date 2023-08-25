Create new messages
===================


Instructions
------------

In the application directory, run the following command:

.. code-block:: console

    $ python manage.py shell_plus

Sample Message list
^^^^^^^^^^^^^^^^^^^

.. code-block:: console

    User = get_user_model()

    Message.objects.create(
        author = User.objects.first(),
        title = "This is a test message in a bottle",
        slug = "this-is-a-test-message-in-a-bottle",
        body = "I'm sending out an S.O.S",
        status = "PB",
    )
    Message.objects.create(
        author = User.objects.get(username="susan"),
        title = "The Waste Land by T.S. Eliot",
        slug = "the-waste-land-by-t-s-eliot",
        body = "April is the cruelest month, breeding\r\n    Lilacs out of the dead land, mixing\r\n    Memory and desire, stirring\r\n    Dull roots with spring rain.",
        status = "PB",
    )
    Message.objects.create(
        author = User.objects.first(),
        title = "Reasons to use a REST framework",
        slug = "reasons-to-use-a-rest-framework",
        body = "Some reasons you might want to use REST framework:\r\n\r\n    The Web browsable API is a huge usability win for your developers.\r\n    Authentication policies including packages for OAuth1a and OAuth2.\r\n    Serialization that supports both ORM and non-ORM data sources.\r\n    Customizable all the way down - just use regular function-based views if you don't need the more powerful features.\r\n    Extensive documentation, and great community support.\r\n    Used and trusted by internationally recognised companies including Mozilla, Red Hat, Heroku, and Eventbrite.",
        status = "PB",
    )
    Message.objects.create(
        author = User.objects.get(username="john"),
        title = "Django is a high-level Python web framework",
        slug = "django-is-a-high-level-python-web-framework",
        body = "Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.",
        status = "PB",
    )
    Message.objects.create(
        author = User.objects.get(username="mary"),
        title = "Ridiculously Fast"
        slug = "ridiculously-fast",
        body = "Django is ridiculously fast. Django was designed to help developers take applications from concept to completion as quickly as possible.",
        status = "PB",
    )
    Message.objects.create(
        author = User.objects.get(username="susan"),
        title = "Reassuringly secure",
        slug = "reassuringly-secure",
        body = "Django is reassuringly secure. Django takes security seriously and helps developers avoid many common security mistakes.",
        status = "PB",
    )
    Message.objects.create(
        author = User.objects.get(username="david"),
        title = "Exceedingly scalable",
        slug = "exceedingly-scalable",
        body = "Some of the busiest sites on the web leverage Django\u2019s ability to quickly and flexibly scale."
        status = "PB",
    )
    Message.objects.create(
        author = User.objects.get(username="alice"),
        title = "Civilization and its Discontents",
        slug = "civilization-and-its-discontents",
        body = "The real problem of humanity is the following: We have Paleolithic emotions, medieval institutions and godlike technology. And it is terrifically dangerous, and it is now approaching a point of crisis overall.",
        status = "PB",
    )
    Message.objects.create(
        author = User.objects.get(username="john"),
        title = "A Painter's Credo of Service to State and Church",
        slug = "a-painters-credo-of-service-to-state-and-church",
        body = "And I have belief As I kneel now and light a candle, sensing A fitted silence in the weight of things. I am a man bound by indentures, agreements. All things dilate On the glory of empires, the prelates' zeal, The Saviour's great goodness in all His forms.",
        status = "PB",
    )
    Message.objects.create(
        author = User.objects.get(username="susan"),
        title = "Eric Dolphy - American Jazz Musician",
        slug = "eric-dolphy-american-jazz-musician",
        body = "Eric Dolphy was an American jazz alto saxophonist, bass clarinetist and flautist. Dolphy was one of several multi-instrumentalists to gain prominence in the same era. Dolphy extended the vocabulary and boundaries of the alto saxophone, and was among the earliest significant jazz flute soloists.",
        status = "PB",
    )
    Message.objects.create(
        author = User.objects.get(username="david"),
        title = "PEP 673 - Self Type
        slug = "pep-673-self-type
        body = "PEP 673 introduces a simple and intuitive way to annotate methods that return an instance of their class. This behaves the same as the TypeVar-based approach specified in PEP 484 but is more concise and easier to follow.",
        status = "PB",
    )
    Message.objects.create(
        author = User.objects.get(username="alice"),
        title = "PEPs are great!",
        slug = "peps-are-great",
        body = "PEPs are a great way of getting the freshest info about what might be included in the upcoming Python releases. So, in this article we will go over all the proposals that are going to bring some exciting new Python features in a near future!",
        status = "PB",
    )
    Message.objects.create(
        author = User.objects.get(username="mary"),
        title = "Your Daily Positive Affirmation",
        slug = "your-daily-positive-affirmation",
        body = "Actively telling yourself that you are smart, funny, interesting, talented, a good communicator, a good friend, unique, knowledgeable, a quick study, an introspective thinker, or whatever other aspect you want to be, will eventually result in you persuading yourself that this is true.",
        status = "PB",
    )

# Sense of Belongingness of a student on-campus

## ABSTRACT

To know the sense of belongingness of a student in the university,
we are designing an app to gather data of how they are feeling at
different locations.The app collects the location data of the student
when he/she is in the premises of university. The App shoots the
relevant questions to find out the belongingness of the student.

Previous studies suggest that students who feel they are
participating tend to find and use campus resources more broadly,
driving their success. Attribution also protects students from stress
and thereby improves their mental health.

While we agree that the characteristics of the environment
influence the way people think, feel, and behave, we disagree
about which aspects of the environment have psychological
consequences. Physical environment, including location, is often
one of the objective characteristics associated with a situation.
The places people visit regularly can be consistently associated
with a set of factors, thus representing a type of situation that has
psychological consequences and has a clear connection with the
individual location.

In addition, it was found that four-year college students with a
high sense of belonging use campus services such as student
counseling and student financial aid more than two-year college
students.

## KEYWORDS

Outlier detection, Sense of belongingness, Community sensing.

## INTRODUCTION:


PROOF OF CONCEPT : The project focuses on retrieving
the location of the user based on the GPS. We are thinking to use
GPS(GPS positioning system) which can be used to get the
accurate location of the user. The App will shoot the questions to
the user based on the user’s location. The questions are asked to
infer whether the student feels that he/she belongs to the
community. The data collected is sent to the Database and is
analyzed using Grafana, a data visualization tool. The user might
get questions in between 2 to 5 questions.


Belonging is an important aspect of college success, whether
it's among classmates, in the classroom, or on campus. It can have
an impact on a student's academic adjustment, achievement, goals,
and even whether or not they continue in school. We know that
belonging is a fundamental human motivation, and that everyone
has a strong need to belong. There are numerous definitions of
belonging. A sense of belonging relates to a sense of togetherness,
of being important or important to others. The lack of a sense of
belonging is commonly referred to as "alienation," "rejection,"
"social isolation," "loneliness," or "marginality," and it has been
connected to negative proximal and long-term consequences like
discontent, low self-esteem, depression.


In this paper we explain how important 'sense of
belongingness' is and what methods have been used to know the
students state of mind. The react-native application collects the
coordinates of location of the user once a day at 11:00 AM. The
coordinates are stored in the database and the notifications are
sent at later time in the day. The questions are shooted based on
the location the student visited when the location was taken from
the user. The future scope of the project would be to analyze
individuals data and display those results to the user.


The surveys are not efficient these days. For example, if the
survey is sent out to 100 people and only 10 % of them would
return with the answers. Due to this very less data points, It is
inefficient to know the problems and how the students are
connected with the campus. We have tried different methods to
motivate students to fill the survey by giving free student cash and
give aways. Even after this marketing strategy we failed to bring
the students for filling the survey. We have analyzed on why
students are not responding to the surveys and had agreed on
terms that students are receiving bulk emails in which our survey
can be missed out. Even though the student opens the survey, he is
not answering all the questions due the size of the questionnaire
as it contains 20 to 25 questions and few questions might not
relate to them. So, In this project we were trying to figure out
what would be the best time to send the survey, how many
questions to send in the survey and what questions to send in the
survey. To collect more data points, we have designed an
application to improve the user experience and sending
personalized notification and location related questions.

Figure 1: **- GPS Location sensing.**

## 1.1 LOCATION

1. The location coordinates are fetched from the network
    provider using the below sample code.

2. If the user is present in a particular location within the
    campus, we retrieve the coordinates else the location data
    will be ignored.
3. We can also find out the congestion in the study areas based
    on the location and people connected to the network.
4. The App shoots the questions if it finds any anomaly in the
    location data.
**Below are steps to find the anomaly in location data:**
1. In order to run anomaly detection job, we must have the
    latitude and longitude.


2. A data visualizer is used like Grafana.
3. An Anomaly detection job should be created to monitor the
    anomalies in data

## 2 .1 GPS Vs Wi-Fi LOCATION:

The way of acquiring location data is the fundamental
distinction between GPS and Wifi locating systems. To
calculate a user's location, GPS uses satellites orbiting the
Earth, whereas Wifi locating technology uses relative
network signal strength acquired from network access
points. Each technology has its own set of advantages and
disadvantages. Let's take a look at a few of them right now.

The Global Positioning System (GPS) is a radio-based
navigation system controlled by the United States
government. You must have a clear line of sight with at least
four GPS satellites in order to use GPS properly. Mountains,
clouds, buildings, and trees all diminish the likelihood of
establishing a successful GPS connection.

Although GPS can locate you everywhere on the earth,
regardless of how far away you are, it is not the most precise
locating technology available. The accuracy of location can
only be as close as 4 meters, or around 13 feet, depending on
the equipment utilized.

When the user is inside a building, surrounded by buildings,
clouds, or trees, however, GPS accuracy is further limited.
As a result, GPS works best in wide places with a clear view
of the terrain.

Cellular location technology is an umbrella word that
encompasses a number of different locating technologies,
such as Wifi and SIM-based approaches.

Cellular appears to fill in the gaps where GPS fails. Its
powers shine in densely populated areas with a high density
of cell towers. Because of how it employs crowdsourced Wi-
Fi data, cellular methods thrive in buildings, cities, and
heavily inhabited locations. It can determine the location of
a device based on its distance from a group of network
access points.

The cellular model's accuracy in locating a user's location
within buildings and places with network coverage is
another advantage. This technology can pinpoint a user's
location to within a few feet, allowing emergency
responders to take more effective action.

## 2 .2 PRIVACY:

## We will ask the user’s permission to access the location of


The user when he or she is in the campus. Location data
outside of the university is not tracked and discarded.


## 2 .3 EMPIRICAL METHODOLOGY:


Procedure :

- Data : We are using the location data generated by the
    application.
1. The application collects the coordinates of location from
    the user.
2. The data will be formatted and sent through a
    messaging queue to the back end.
3. Back end stores the data in database and process that
    data to identify if it is an outlier.
4. If there is a pattern change the application sends a
    survey to the user.

## 2.3 METHODS

#### I. USER'S MOST VISITED PLACE:

**1.** User's most visited place place is determined by taking the
location data of the user and the data is undergone through cluster
analysis. The cluster with most points is taken as the location that
is spent most of the time on that particular day.

#### II. GENERATING QUESTIONS:


1.Once we get the user's most visited location, the questionnaire
is prepared based on the location. The number of questions
will be decided based on the previous answers he/she
provided.


#### III. STORING ANSWERS:

1**.** Answers are stored in the database with the timestamp of when


## 5. FUTURESCOPE:

1.We can generate more personalized survey questions for the
user.

2. Displaying the analysis of their mood in various locations.
3. Visualization of the time the user spent most at various
locations in the campus.
4. Projecting all the data points of location on the map to find out
the density population at each of the study spaces which might
look like the below image figure 2.


## 6. CONCLUSION:


We developed an app to improve the sense of belongingness
among the students at the university. The application collects the
coordinates of the location data daily and stores it in a database.
At the later time of the day the location data is analyzed and a
survey is sent out to the user based on the location they visited
when the location was tracked. The number of questions in the
questionnaire varies from two to five and location specific
questions were sent.

Questions that we used in the survey are:

1. I feel a connection with the CU Boulder community.
2. I feel like I fit in at CU Boulder.
3. I feel that I belong at CU Boulder.
4. I view CU Boulder as my home during my undergraduate
years.
5. People on campus are generally supportive of my individual
needs.
6. There are people on campus who are genuinely interested in
me as a person.
7. There are people on campus who care about my future.
8. At CU, I’m treated like I belong.
9. I have a sense of community at CU.
10. I feel valued.
11. I am proud to be a student at CU.
12. I feel supported.

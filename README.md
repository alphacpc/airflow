# **A Découverte de** 

![Filtres](./images/logo.png)
<br></br>
<br></br>

## **Architecture basique de Airflow**

![Filtres](./images/architecture.png)
<br></br>
<br></br>

## **Présentation**
> - ### Airflow est une plateforme permettant (le CPC) de **créer**, de **planifier** et de **contrôler** des flux de travail,
> - ### Initialement, c’est **Airbnb** qui a démarré ce projet en octobre 2014,
> - ### afin de **gérer les flux de travail de plus en plus complexes** au sein de l'entreprise,
> - ### Dès le début, le projet a été rendu *open source*,
> - ### devenu un projet de l'incubateur Apache en mars 2016,
> - ### Considéré comme *"top level project"* par Apache Software Foundation en janvier 2019,
> - ### Airflow est écrit en **Python**
> - ### *les workflows*  sont créés via des scripts *Python*. 
> - ### Airflow est conçu selon le principe de la "configuration as code" ([Ansible](https://www.ansible.com/) ou [Terraform](https://www.terraform.io/)).
> - ### L'utilisation de Python permet aux développeurs d'importer des bibliothèques et des classes pour les aider à créer leurs workflows. 


<br></br>

## **Principe**

> - ### **<span style='color:#F05'>Dynamique :</span>** Les pipelines Airflow sont configurés en tant que code (Python), ce qui permet la génération dynamique de pipelines. Cela permet d'écrire du code qui instancie les pipelines de façon dynamique.
> - ### **<span style='color:#1ABC'>Extensible :</span>** Définissez facilement vos propres opérateurs, exécuteurs et étendez la bibliothèque pour qu'elle corresponde au niveau d'abstraction qui convient à votre environnement.
> - ### **<span style='color:orange'>Élégant :</span>** Les pipelines Airflow sont légers et explicites. Le paramétrage de vos scripts est intégré au cœur d'Airflow grâce au puissant moteur de modélisation Jinja.
> - ### **<span style='color:yellow'>Evolutif :</span>** Airflow a une architecture modulaire et utilise une file de messages pour orchestrer un nombre arbitraire de travailleurs. Airflow est prêt à évoluer à l'infini.

<br></br>
## **Ce qu’il faudrait comprendre**
> - ### Airflow n'est pas une solution de streaming de données. 
> - ### Les tâches ne déplacent pas les données de l'une à l'autre (bien que les tâches puissent échanger des métadonnées !). 
> - ### Airflow n'est pas dans l'espace Spark Streaming ou Storm, il est plus comparable à Oozie ou Azkaban.
> - ### On s'attend à ce que les flux de travail soient principalement statiques ou évoluent lentement. 



<br></br>
## **Caractéristiques**
> - ### Pure Python
> - ### Interface utilisateur pratique
> - ### Intégrations robustes
> - ### Simplicité d'utilisation
> - ### Open source


<br></br>
## **Installation**
> 1. ### Via **[Python](https://github.com/apache/airflow#installing-from-pypi)**
> 2. ### Via **[Docker](https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html)**


<br></br>
## **1. Lancer Airflow (Python)**

> ## export AIRFLOW_HOME=~/airflow

> ## airflow db init

> ## airflow users create --username admin --firstname alpha --lastname DIALLO --role Admin --email alpha@admin.sn

> ## airflow webserver -p 4040


<br></br>
## **2. Lancer Airflow (Docker)**

> ## docker-compose up airflow-init

> ## docker-compose up -d

#### **NB:** S'assurer que la version de docker-compose soit **1.29.1** ou **+**
# dbt-upsolver
# Using Upsolver udapter for dbt


## What is Upsolver

[Upsolver](https://upsolver.com) enables you to use familiar SQL syntax to quickly build and deploy data pipelines, powered by a stream processing engine designed for cloud data lakes.

## SQLake

[SQLake](https://docs.upsolver.com/sqlake) is Upsolvers new UI and SQL console allowing to execute commands and monitor pipelines in the UI. It also includes freee trial and access to variety of examples and tutorials.

## What is dbt
[dbt](https://docs.getdbt.com/) is a transformation workflow that helps you get more work done while producing higher quality results.

## What is dbt Core
dbt Core is an open-source tool that enables data teams to transform data using analytics engineering best practices. You can install and use dbt Core on the command line.

## Getting started  

### Install dbt-upsolver adapter :

```sh
 pip install  dbt-upsolver
```
### Make sure the adapter is installed:
```sh
dbt --version
```
#### Expect to see:
```
Core:
  - installed: <version>
  - latest:    <version>
Plugins:
  - upsolver: <version>
```
### Register Upsolver account

To register just navigate to [SQL Lake Sign Up form](https://sqlake.upsolver.com/signup). You'll have access to SQL workbench with examples and tutorials after completing the registration.

### Create API token

After login navigate to "[Settings](https://sqlake.upsolver.com/Settings)" and then to "[API Tokens](https://sqlake.upsolver.com/Settings/api-tokens)"
You will need API token and API Url to access Upsolver programatically.
Settings -> API Tokens -> Generate
Then click "Generate" new token and save it for future use.

### Get your user name, database and schema
For **user name** navigate to **Settings** -> **User details** and copy user name
For **database** and **schema** navigate to **Worksheets** and click **New**.
You will find **database name** and **schema(catalog) name** under **Entities panel**

###  Create new dbt-upsolver project
```sh
dbt init <project_name>
```
Prompt:

Which database would you like to use?
[1] upsolver

```sh
Enter a number:
api_url (your api_url): https://mt-api-prod.upsolver.com
token (your token): <token>
user (dev username): <username>
database (default database): <database>
schema (default schema): <schema>
threads (1 or more) [1]: <number>
```

####  profiles.yml should look like this:
###### profiles.yml location is something like /Users/<user>/.dbt/profiles.yml
```yml
project_name:
  target: dev
  outputs:
    dev:
      api_url: https://mt-api-prod.upsolver.com
      database: ...
      schema: ...
      threads: 1
      token: ...
      type: upsolver
      user: ...
```

### Check connection
```sh
dbt debug
```
#### Run all models
```sh
dbt run
```
#### Run the specific model
```sh
dbt run --select <model name>
```
### Supported dbt commands:
- dbt init
- dbt debug
- dbt run
- dbt compile


## Further reading
[Projects samples examples](https://github.com/Upsolver/dbt-upsolver/tree/main/examples)
[Upsolver sqlake documentation](https://docs.upsolver.com/sqlake/)
[Upsolver sqlake documentation](https://docs.getdbt.com/docs/introduction)

jewel
=====

To view deployed version in browser:
  heroku open

To push to heroku:
  git push heroku master

To push to github:
  git push origin master

To enter virtualenv before running anything:
 source venv/bin/activate

To run local server:
  foreman start

To run python shell:
  heroku run python

To view heroku logs:
  heroku logs

To run javascript tests:
  scripts/run_tests.sh

To run python tests:
  python py_tests/runner.py

To start the local redis server:
  redis-server

To run inside a docker container
--------------------------------

You can now build, package and run this microservice using Docker.

Now you can build your docker image by entering from a terminal where you have access to Docker, execute the following command:

```shell
> ./mvnw clean package docker:build
```

Even push it to a repository of your choice:

```shell
> ./mvnw clean package docker:build -DpushImage
```

FROM java:8-jre

COPY @project.build.finalName@.jar /opt/build/

WORKDIR /opt/build

EXPOSE 8080

CMD ["java", "-Xmx1g", "-jar", "@project.build.finalName@.jar"]

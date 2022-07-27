FROM alpine


ENV ENVIRONMENT=dev
ENV HOST=0.0.0.0
ENV PORT=8080

# must match the CMD/ENTRYPOINT binary path, and RUN/CMD/ADD all use WORKDIR
WORKDIR /my_app


RUN apk add python3 py3-pip

COPY requirements.txt ./
RUN /usr/bin/pip3 install -r requirements.txt

# src is the relative path of build context, the dest is the relative path of WORKDIR
# not working
#   ADD ./src ./  if <src> is a folder, ADD only copy files in the folder, but not the folder
#   ADD ./src /myapp/ ???
# works
#   ADD ./src/* ./src/    tailling slash in the destination means it's a folder
#   ADD ./src ./src/
COPY ./src ./src


CMD python3 /my_app/src/app.py --env ${ENVIRONMENT} ${HOST} ${PORT}

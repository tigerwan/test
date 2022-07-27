FROM centos:7


ENV ENVIRONMENT=dev
ENV HOST=0.0.0.0
ENV PORT=8080
# add pip3 path in the PATH so that no need to give the pip3 full path the subseqent instruction
ENV PATH=$PATH:/usr/bin

# must match the CMD/ENTRYPOINT binary path, and RUN/CMD/ADD all use WORKDIR
WORKDIR /my_app

# reduce layers by combining multiple RUN
RUN yum install -y python3 && yum install -y python3-pip

COPY requirements.txt ./

RUN pip3 install -r requirements.txt

# src is the relative path of build context, the dest is the relative path of WORKDIR
# not working
#   ADD ./src ./  if <src> is a folder, ADD only copy files in the folder, but not the folder
#   ADD ./src /myapp/ ???
# works
#   ADD ./src/* ./src/    tailling slash in the destination means it's a folder
#   ADD ./src ./src/
COPY ./src ./src

# if using CMD ["python3", "/my_app/src/app.py", "--env", "${ENVIRONMENT}", "${HOST}","${PORT}"],${ENVIRONMENT}/${HOST}/${PORT} are not expanded at all
CMD python /my_app/src/app.py --env ${ENVIRONMENT} ${HOST} ${PORT}

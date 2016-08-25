#
# Base Docker instance used for building an Amazon AMI
#
FROM centos:latest

RUN yum -y install epel-release
RUN yum clean all
RUN yum -y install \
    python-lxml \
    unzip \
    openssh \
    openssh-clients


COPY packer-installer.py /tmp/
RUN /tmp/packer-installer.py

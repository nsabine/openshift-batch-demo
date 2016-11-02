FROM fedora
MAINTAINER nsabine@redhat.com

RUN dnf update -y && \
    dnf install -y https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm && \
    dnf install -y TestU01 TestU01-devel gcc && \
    dnf clean all

RUN gcc -c /usr/share/TestU01/examples/my16807.c -I/usr/share/TestU01/include/
ADD ./ex8.c /ex8.c
RUN gcc ex8.c my16807.o -o test -ltestu01 -lmylib -I /usr/share/TestU01/include/ -I /usr/share/TestU01/examples/ -L /usr/share/TestU01/lib/

CMD /test


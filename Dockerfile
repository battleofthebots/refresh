FROM ghcr.io/battleofthebots/botb-base-image:ubuntu as build

WORKDIR /opt
COPY requirements.txt pycompile.py router.py ./
RUN pip3 install -r requirements.txt
RUN python3 /opt/pycompile.py

FROM ghcr.io/battleofthebots/botb-base-image:ubuntu as run

WORKDIR /opt
COPY --from=build /opt/__pycache__/router.cpython-38.pyc /opt/router.cpython-38.pyc
COPY requirements.txt .
RUN pip install -r requirements.txt
USER user
ENTRYPOINT python3 /opt/router.cpython-38.pyc

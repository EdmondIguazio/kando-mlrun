FROM mlrun/mlrun:0.9.1

ARG GITHUB_ACCESS_TOKEN
RUN apt update
RUN apt-get install -y python3-dev
RUN pip install --no-cache-dir lightgbm==3.1.1
RUN pip install --no-cache-dir pandas==1.2.2
RUN pip install --no-cache-dir pickle5==0.0.11
RUN pip install --no-cache-dir pycwt~=0.3.0a22
RUN pip install --no-cache-dir pathlib==1.0.1
RUN pip install --no-cache-dir pytz==2020.1
RUN pip install --no-cache-dir pandas~=1.1.3
RUN pip install --no-cache-dir plotly
RUN pip install --no-cache-dir vecstack~=0.4.0
RUN pip install --no-cache-dir flask~=1.1.1
RUN pip install --no-cache-dir numpy~=1.21.0
RUN pip install --no-cache-dir requests-oauthlib~=1.3.0
RUN pip install --no-cache-dir requests-toolbelt~=0.9.1
RUN pip install --no-cache-dir scikit-learn~=0.22.1
RUN pip install --no-cache-dir vecstack~=0.4.0
RUN pip install --no-cache-dir scipy~=1.6.1
RUN pip install --no-cache-dir python-dotenv==0.15.0
RUN pip install --no-cache-dir gradient==1.4.2
RUN pip install git+https://$GITHUB_ACCESS_TOKEN@github.com/nadavk72/kando-python-client.git@0.0.30
RUN pip install git+https://$GITHUB_ACCESS_TOKEN@github.com/kando-env/ML_models.git@master


CMD ["sh"]
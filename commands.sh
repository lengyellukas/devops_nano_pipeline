git clone git@github.com:lengyellukas/devops_nano_pipeline.git
cd devops_nano_pipeline
make install
git pull
make all
az webapp up -n devops-nano-pipeline
git add .
git commit -m "commit message"
git push
./make_predict_azure_app.sh
locust

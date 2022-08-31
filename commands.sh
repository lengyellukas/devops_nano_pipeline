git clone git@github.com:lengyellukas/devops_nano_pipeline.git
cd devops_nano_pipeline
git pull
make all
az webapp up -n devops_nano_pipeline
./make_predict_azure_app.sh

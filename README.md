# {{ values.repoName }}

{{ values.description }}

## Overview

This is a {{ values.appType }} built with {{ values.appLanguage }}, created using the Backstage GitHub Repository Generator template.

## Features

- **Application Type**: {{ values.appType }}
- **Runtime**: {{ values.appLanguage }}
- **Port**: {{ values.port }}

- **Containerized**: Docker support included


- **Kubernetes Ready**: Helm charts included


- **Auto-scaling**: Horizontal Pod Autoscaler configured ({{ values.minReplicas }}-{{ values.maxReplicas }} replicas)


- **Health Checks**: Liveness and readiness probes configured


## Getting Started

### Prerequisites


- Python 3.11+
- pip


- Docker (for containerization)


- Kubernetes cluster (for deployment)
- Helm 3+ (for chart deployment)


### Local Development

1. Clone the repository:
   ```bash
   git clone https://github.com/{{ values.repoOwner }}/{{ values.repoName }}.git
   cd {{ values.repoName }}
   ```

2. Install dependencies:
   
   ```bash
   pip install -r requirements.txt
   ```
   

3. Start the application:
   
   ```bash
   python app.py
   ```
   

The application will be available at `http://localhost:{{ values.port }}`


### Health Checks

- **Health**: `GET /health` - Application health status
- **Readiness**: `GET /ready` - Application readiness status



## Docker

### Build the Docker image:
```bash
docker build -t {{ values.repoOwner }}/{{ values.repoName }}:latest .
```

### Run the container:
```bash
docker run -p {{ values.port }}:{{ values.port }} {{ values.repoOwner }}/{{ values.repoName }}:latest
```



## Kubernetes Deployment

### Using Helm

1. Install the Helm chart:
   ```bash
   helm install {{ values.repoName }} ./infrastructure/helm
   ```

2. Upgrade the deployment:
   ```bash
   helm upgrade {{ values.repoName }} ./infrastructure/helm
   ```

3. Uninstall:
   ```bash
   helm uninstall {{ values.repoName }}
   ```

### Configuration

The Helm chart supports the following key configurations:

- **Replicas**: {{ values.replicas }} (initial)

- **Auto-scaling**: {{ values.minReplicas }}-{{ values.maxReplicas }} replicas
- **CPU Threshold**: {{ values.cpuThreshold }}%
- **Memory Threshold**: {{ values.memoryThreshold }}%

- **Resources**:
  - CPU: {{ values.cpuRequest }} (request), {{ values.cpuLimit }} (limit)
  - Memory: {{ values.memoryRequest }} (request), {{ values.memoryLimit }} (limit)

- **Service Type**: {{ values.serviceType }}



### Customize Values

Edit `infrastructure/helm/values.yaml` to customize the deployment according to your needs.


## Project Structure

```
{{ values.repoName }}/
├── README.md
├── catalog-info.yaml          # Backstage catalog definition

├── Dockerfile                 # Container definition


└── infrastructure/
    └── helm/                  # Helm chart
        ├── Chart.yaml
        ├── values.yaml
        └── templates/
            ├── deployment.yaml
            ├── service.yaml

            ├── hpa.yaml       # Horizontal Pod Autoscaler


            └── ...

```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For questions or support, please contact the platform team or create an issue in this repository.

# Nestok Test Collection - README  

The app is built using **FastAPI**, integrates **Firebase**, and includes Docker and Google Cloud Deployment.

## Firebase Setup  

1. Visit the [Firebase Console](https://console.firebase.google.com).  
2. **Create a new project**: Follow the on-screen instructions.  
   - Google Analytics integration is optional.  
3. **Create a web app**: Copy the Firebase configuration.  
4. Save it in `firebase_config.json`, on the root directory.

## Local Development Setup  
1. **Clone the repository**:  
   ```bash
   git clone https://github.com/iABn0rma1/FastAPI-FirebaseWrapper.git
   cd FastAPI-FirebaseWrapper
   ```  

2. **Install dependencies**:  
   ```bash
   pip install -r requirements.txt
   ```  

3. **Run the application**:  
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8080
   ```  

   The app will be live on `http://localhost:8080`.

---

### Push Docker Image to Google Cloud
1. **Initialize Google Cloud CLI**:  
   ```bash
   gcloud init
   ```  

2. **Tag and push the Docker image**:  
   ```bash
   gcloud builds submit --tag gcr.io/newstok-test-collection/image
   ```

3. Deploy the container to **Google Cloud Run**:  
   ```bash
   gcloud run deploy --image gcr.io/newstok-test-collection/image --platform managed
   ```

For detailed instructions, refer to this [guide on Medium](https://medium.com/codex/secured-serverless-fastapi-with-google-cloud-run-66242b916b46).  


## API Endpoints Overview  

### 1. Basic Endpoints  
| **Endpoint**                 | **Method**   | **Description**                    |  
|------------------------------|--------------|------------------------------------|  
| `/hello`                     | `GET`        | Returns a "Hello World" message.   |  
| `/add`                       | `POST`       | Adds a timestamp to Firestore.     |  

### 2. FakeStore API Wrapper  
| **Endpoint**                 | **Method**   | **Description**                    |  
|------------------------------|--------------|------------------------------------|  
| `/products`                  | `GET`        | Fetches the list of products.      |  
| `/cart/add/{product_id}`     | `POST`       | Add a product in cart.             |  
| `/cart`                      | `GET`        | Fetches products in cart.          |  

---

> [!NOTE]
> - The default **user ID** is `1` for all cart-related operations.  
> - The default purchasing **quantity** of products is also `1`.
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
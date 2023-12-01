# url-shortener: In Progress
url shortening project that will be completed in phases. 

Tools: Python, FastAPI, Docker, Amazon Web Services (EC2, S3, DynamoDB), Postman


### Functional Requirements:
#### 1. Create short URLs: 
- URL validation will be implemented to ensure that the service isn't being used to distribute malicious links.
- URL character limits will be implemented based on the typical use case and technical constraints.
#### 2. Get Original URL given a short URL: 
Users should be able to retrieve the original URL associated with a short URL they have generated or obtained. If the shortened URL link is shared, anyone who clicks the link should be redirected to the original link. 
#### 3. List all short URLs and original URL pairs: 
Authorized users should be able to see a list of all short URLs and their respective URL pairs.

### Non - Functional Requirements:
#### 1. Short URL must not have any collisions - 
When adding or creating a short URL, we need to ensure that the short URL must not already exist in the Database. If it does, we need to regenerate the short URL, if no custom short URL is provided.
#### 2. URL must be secure - 
The URL shortener must implement robust security measures to protect user data, prevent unauthorized access, and mitigate common web vulnerabilities
- URL shortener will operate over HTTPS
- Standard authentication and authorization mechanisms will control who can perform CRUD operations on the URLs.
- URL shortener will only store necessary user data.
- Input validation will be used to prevent common security threats.
- Rate limiting will be implemented to control traffic and maintain a high quality of service.
#### 3. The APIs accessible to the public must be performant
The service should provide low-latency responses for URL redirection. The time taken to resolve a short URL to its original long URL should be minimal.
- Database queries will be optimized for efficient queries for up to 100 users (proper indexing).
- Caching will be used to allow quicker retrieval of frequently used data.
- Load balancing will be used to distribute incoming traffic across multiple servers or instances to prevent overload and ensure a more responsive service.
- Monitoring of API performance will be used to identify bottlenecks or performance issues and provide efficient troubleshooting.
#### Maintainability and Observability 
- The system will be designed in a modular way so that it's easy to add new features or make changes without affecting the entire codebase.
Version control will be used to track changes and allow collaboration.
- Monitoring and logging mechanisms will be implemented  to track system performance, detect issues, and troubleshoot problems quickly.

### Assumptions
- The service will be accessed by less than 100 users.
- Scalability is not a concern for the first Phase.


### API
#### 1. ​POST /shorten_url(url, short_url: optional)
##### Description: Allows users to provide a URL to shorten with the option to provide a custom, shortened URL.

##### Input: Request should include a valid URL. Requests may include an optional custom URL. 
##### Output: API will respond with either a successful POST or failed POST.
- If successful, API will respond with a confirmation of POST request with the original URL and the custom URL in the response. 
- If failed, the API will respond with the corresponding error message. 

##### Error Conditions: API will handle the following error conditions:
- Invalid URL - If the input URL is not a valid URL, the API will respond with an error message.
- Shortened URL taken - If the custom shortened URL is already in use, the API will respond with an error indicating that the chosen URL is not available.
- Character limit exceeded - If the user-provided URL exceeds a predefined character limit, the API will respond with an error indicating that the URL is too long.
- Unexpected error (catch all) - In the event of an unexpected server error or an issue not covered by the specific error conditions above, the API will provide a generic error response.
- Unauthorized access - If a user attempts to access this endpoint without proper authentication or authorization, the API will respond with an error indicating unauthorized access.

#### 2. GET /list_urls
##### Description: Allows authorized users to retrieve a list of all relevant shortened URLs and their respective original URLs. 

##### Input: When this is called, the system will need to ensure the user is authenticated and authorized to access the information.

##### Output: API will respond with either a successful or failed GET. 
- If successful, API will respond with a list of shortened URLs (key) and their corresponding URLs (value) in a key: value format.
- If failed, the API will respond with the corresponding error message. 

##### Error Conditions: API will handle the following error conditions:
- Unauthorized access - If a user attempts to access this endpoint without proper authentication or authorization, the API will respond with an error indicating unauthorized access.
- Unexpected error (catch all) - In the event of an unexpected server error or an issue not covered by the specific error conditions above, the API will provide a generic error response.

#### 3. GET /redirect(short_url)
##### Description: Redirects the user to the appropriate URL based on the shortened URL when a GET redirect request is made.

##### Input: Request will include a valid short URL. When this is called, the system will need to ensure the user is authenticated and authorized to access the information.

##### Output: API will respond with either a successful or failed GET. 
- If successful, The API will provide the appropriate URL for a valid request.
- If failed, the API will respond with the corresponding error message.

##### Error Conditions: API will handle the following error conditions:
- Invalid URL - If the input URL is not a valid shortened URL, the API will respond with an error message.
- Unauthorized access - If a user attempts to access this endpoint without proper authentication or authorization, the API will respond with an error indicating unauthorized access.
- Unexpected error (catch all) - In the event of an unexpected server error or an issue not covered by the specific error conditions above, the API will provide a generic error response.

  

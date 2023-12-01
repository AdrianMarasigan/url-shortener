# url-shortener: In Progress

Tools: Python, FastAPI, Docker, Amazon Web Services (EC2, S3, DynamoDB), Postman


## Functional Requirements:
### Create short URLs: 
- URL validation will be implemented to ensure that the service isn't being used to distribute malicious links.
- URL character limits will be implemented based on the typical use case and technical constraints.
### Get Original URL given a short URL: 
Users should be able to retrieve the original URL associated with a short URL they have generated or obtained. If the shortened URL link is shared, anyone who clicks the link should be redirected to the original link. 
### List all short URLs and original URL pairs: 
Authorized users should be able to see a list of all short URLs and their respective URL pairs.

## Non - Functional Requirements:
### Short URL must not have any collisions - 
When adding or creating a short URL, we need to ensure that the short URL must not already exist in the Database. If it does, we need to regenerate the short URL, if no custom short URL is provided.
### URL must be secure - 
The URL shortener must implement robust security measures to protect user data, prevent unauthorized access, and mitigate common web vulnerabilities
- URL shortener will operate over HTTPS
- Standard authentication and authorization mechanisms will control who can perform CRUD operations on the URLs.
- URL shortener will only store necessary user data.
- Input validation will be used to prevent common security threats.
- Rate limiting will be implemented to control traffic and maintain a high quality of service.
### The APIs accessible to the public must be performant
The service should provide low-latency responses for URL redirection. The time taken to resolve a short URL to its original long URL should be minimal.
- Database queries will be optimized for efficient queries for up to 100 users (proper indexing).
- Caching will be used to allow quicker retrieval of frequently used data.
- Load balancing will be used to distribute incoming traffic across multiple servers or instances to prevent overload and ensure a more responsive service.
- Monitoring of API performance will be used to identify bottlenecks or performance issues and provide efficient troubleshooting.
### Maintainability and Observability 
- The system will be designed in a modular way so that it's easy to add new features or make changes without affecting the entire codebase.
Version control will be used to track changes and allow collaboration.
- Monitoring and logging mechanisms will be implemented  to track system performance, detect issues, and troubleshoot problems quickly.

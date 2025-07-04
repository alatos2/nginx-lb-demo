# Example: NGINX as a load balancer, reverse proxy and HTTP cache

### Scenario: We have two backend applications running on http://localhost:8080 (within a Docker container). We want NGINX to serve as the public-facing entry point, listening on port 80, and forwarding requests to this backend.

### To test for load balancing and reverse proxy:
1. docker-compose up --build -d
2. curl http://localhost:8080/

### To test for caching:
1. docker-compose up --build -d
2. curl -I http://localhost:8080/ # Use -I to see only headers

- Look for the X-Cache-Status header. It should likely say MISS. This means NGINX didn't find the content in its cache, so it fetched it from the backend.
- Subsequent Requests (within 60 seconds): This time, the X-Cache-Status header should say HIT. This confirms that NGINX served the content directly from its cache without contacting the backend server. You can also verify by checking the backend server's logs (e.g., docker logs app_backend). You should see the initial request hitting the backend, but not subsequent ones after the HIT.
- Wait for more than 60 seconds (or whatever proxy_cache_valid you set). Then, make another request.
- The X-Cache-Status will likely revert to MISS again, as the cached item has expired and NGINX will re-fetch it from the backend

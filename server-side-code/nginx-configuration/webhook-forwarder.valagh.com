server {
	listen 443 ssl;
	listen [::]:443 ssl;

	server_name webhook-forwarder.valagh.com;
	
	ssl_certificate     "[redacted]"/fullchain.com.cer;
	ssl_certificate_key "[redacted]"/wehook-forwarder.valagh.com.key;
	ssl_protocols       TLSv1.1 TLSv1.2;
	ssl_ciphers         HIGH:!aNULL:!MD5;
	
	location /"[redacted]" {
		include uwsgi_params;
        uwsgi_pass unix:"[redacted]"/listener.sock;
	}

	error_page 404 = @400;         # Invalid paths are treated as bad requests
    proxy_intercept_errors on;     # Do not send backend errors to the client
    default_type application/json; # If no content-type then assume JSON
}



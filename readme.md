This is the initial code for countyroadcanning.us as of 1/11/24

This is my mother-in-law's website that I'm creating for her. 
This is my initial commit of the code. I had previously created her website with flask
and now I have learned the error of my ways and have moved to Django.. A lot of the
stuff I need for her to be able to update the website (adding and removing products, blogging, etc) 
are already available through django's admin interface. 

I'm working out the process to dockerize this application and properly deploy it to production when 
it's ready for the big time. I'm currently using whitenoise to serve static files. 

I've run into a bit of a kink with serving the media files however. The media files being product images and such.
I want her to be able to create new products and add images for the new products, but it seems I'm going to have to 
serve those media files through nginx. So I've included an nginx.conf as a template to get me started. 

I want to include some CI/CD in this project. It's all kind of in the planning phase really. But I've put together
a simple prototype for what I'm trying to do. It's 4:05AM right now, I think I'm done with this for the night. 

## DevOps 
* dockerize django app


## Incomplete
* Stripe integration
* Shopping cart
* UI

## Complete
* Nothing.


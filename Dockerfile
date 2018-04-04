FROM nginx:alpine

COPY nginx/gem_molo_unicore.conf /etc/nginx/conf.d/gem_molo_unicore.conf

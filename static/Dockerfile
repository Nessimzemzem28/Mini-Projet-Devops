# Build stage
FROM node:18 AS build
WORKDIR /app
COPY package*.json ./
RUN npm install --legacy-peer-deps
COPY . .
RUN npm run build

# Production stage with Nginx
FROM nginx:alpine
COPY --from=build /app/build /usr/share/nginx/html
# copy custom nginx config
COPY default.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

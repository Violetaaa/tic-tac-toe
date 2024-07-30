FROM node:20-alpine
EXPOSE 5173
WORKDIR /usr/src/app
COPY . .
RUN npm install
CMD npm run dev --host=0.0.0.0 --port=5173


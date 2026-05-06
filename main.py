from fastapi import FastAPI
import searoute as sr

app = FastAPI()

@app.get("/get_route")
def get_route(lat1: float, lon1: float, lat2: float, lon2: float):
    # searoute [longitude, latitude] formatını bekler
    origin = [lon1, lat1]
    destination = [lon2, lat2]
    
    # Deniz rotasını hesapla
    route = sr.searoute(origin, destination)
    
    # Sonucu (GeoJSON) geri döndür
    return route

# Çalıştırmak için: pip install fastapi uvicorn searoute
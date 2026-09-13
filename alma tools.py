import tkinter as tk
from tkinter import messagebox, filedialog
import folium
from shapely.geometry import Polygon
import datetime
import random

class AgriMonitorSatelit:
    def __init__(self, root):
        self.root = root
        self.root.title("Agriculture land mapping")
        self.root.geometry("400x550")
        self.root.configure(bg="#f0f0f0")

        self.coords = []

# set UI
        tk.Label(root, text="ALMA TOOLS", font=("Helvetica", 16, "bold"), bg="#f0f0f0", fg="#2e7d32").pack(pady=15)

        frame_input = tk.Frame(root, bg="#f0f0f0")
        frame_input.pack(pady=10)

        tk.Label(frame_input, text="Latitude :", bg="#f0f0f0").grid(row=0, column=0, sticky="w")
        self.lat_entry = tk.Entry(frame_input, width=25)
        self.lat_entry.grid(row=0, column=1, pady=5)

        tk.Label(frame_input, text="Longitude :", bg="#f0f0f0").grid(row=1, column=0, sticky="w")
        self.long_entry = tk.Entry(frame_input, width=25)
        self.long_entry.grid(row=1, column=1, pady=5)

        tk.Button(root, text="Tambah Titik Koordinat", command=self.add_coordinate, bg="#4caf50", fg="white", relief="flat").pack(pady=5)
        
        self.listbox = tk.Listbox(root, height=8, width=50)
        self.listbox.pack(pady=10, padx=20)

# button execution
        btn_frame = tk.Frame(root, bg="#f0f0f0")
        btn_frame.pack(pady=15)
        
        tk.Button(btn_frame, text="Generate", command=self.generate_report, bg="#1976d2", fg="white", width=20).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Reset", command=self.reset, bg="#e53935", fg="white", width=10).pack(side=tk.LEFT, padx=5)

    def add_coordinate(self):
        try:
            lat = float(self.lat_entry.get())
            lon = float(self.long_entry.get())
            self.coords.append((lat, lon))
            self.listbox.insert(tk.END, f"Titik {len(self.coords)}: [{lat}, {lon}]")
            self.lat_entry.delete(0, tk.END)
            self.long_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Input harus berupa angka koordinat!")

    def get_analysis_logic(self, poly):

        centroid = poly.centroid
        area_m2 = poly.area * (111320**2) 
        
        temp = 24 + (centroid.y % 6)
        hum = 60 + (centroid.x % 25)
        light = 800 + (centroid.y % 150)
        
        struct_list = ["Lempung Berpasir", "Tanah Aluvial", "Tanah Gambut", "Tanah Liat"]
        struct = struct_list[int(centroid.x * 100) % len(struct_list)]
        
        return {
            "area": round(area_m2, 2),
            "temp": round(temp, 1),
            "humidity": round(hum, 1),
            "soil": struct,
            "light": round(light, 0)
        }

    def generate_report(self):
        if len(self.coords) < 3:
            messagebox.showwarning("Warning", "Masukkan minimal 3 titik koordinat!")
            return

        poly = Polygon(self.coords)
        data = self.get_analysis_logic(poly)
        center = [poly.centroid.y, poly.centroid.x]

# create maps by Tile Satelit Esri
        m = folium.Map(
            location=[self.coords[0][0], self.coords[0][1]], 
            zoom_start=18,
            tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
            attr='Esri World Imagery'
        )

        folium.Polygon(
            locations=self.coords,
            color="#ADFF2F", # Border lime green
            weight=2,
            fill=True,
            fill_color="#228B22", # Forest Green
            fill_opacity=0.5,
            popup=f"Area Terdeteksi: {data['area']} m2"
        ).add_to(m)

# Style out HTML
        html_popup = f"""
        <div style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; size: 12px; color: #333;">
            <h3 style="color: #2e7d32; margin-bottom: 5px;">Analisis Lahan</h3>
            <table style="width: 100%; border-collapse: collapse;">
                <tr style="background: #f2f2f2;"><td style="padding: 5px;"><b>Luas Lahan</b></td><td style="padding: 5px;">: {data['area']} m²</td></tr>
                <tr><td style="padding: 5px;"><b>Suhu Udara</b></td><td style="padding: 5px;">: {data['temp']} °C</td></tr>
                <tr style="background: #f2f2f2;"><td style="padding: 5px;"><b>Kelembaban</b></td><td style="padding: 5px;">: {data['humidity']} %</td></tr>
                <tr><td style="padding: 5px;"><b>Struktur Tanah</b></td><td style="padding: 5px;">: {data['soil']}</td></tr>
                <tr style="background: #f2f2f2;"><td style="padding: 5px;"><b>Intensitas Cahaya</b></td><td style="padding: 5px;">: {data['light']} Lux</td></tr>
            </table>
            <p style="font-size: 10px; color: gray; margin-top: 10px;">Data diproses pada : {datetime.datetime.now().strftime('%H:%M:%S')}</p>
        </div>
        """
        
        folium.Marker(
            location=[self.coords[0][0], self.coords[0][1]],
            icon=folium.Icon(color="green", icon="leaf"),
            popup=folium.Popup(html_popup, max_width=300)
        ).add_to(m)

# saved
        save_path = filedialog.asksaveasfilename(defaultextension=".html", filetypes=[("HTML files", "*.html")])
        if save_path:
            m.save(save_path)
            messagebox.showinfo("Succeed", "Visualization has been saved!")

    def reset(self):
        self.coords = []
        self.listbox.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = AgriMonitorSatelit(root)
    root.mainloop()
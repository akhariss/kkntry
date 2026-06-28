FROM odoo:19

# Copy module ke folder Odoo
COPY . /mnt/extra-addons/kkntry

# Expose port
EXPOSE 8069

# Jalankan Odoo
CMD ["odoo", "-c", "/etc/odoo/odoo.conf"]


# ML-Based Network Intrusion Detection System

This project demonstrates a machine learning-based Network Intrusion Detection System (NIDS) using the CICIDS2017 dataset. It includes both Random Forest and Deep Learning models for detecting DDoS, port scan, and other network threats in real time.

## Features
- Trains Random Forest and Deep Learning models on CICIDS2017 for DDoS/port scan/threat detection.
- Real-time packet capture and classification with Scapy.
- Modular code for easy extension and integration.
- Output logging for real-time predictions.

## Getting Started

1. **Install requirements:**  
   `pip install -r requirements.txt`
2. **Download the CICIDS2017 dataset** and place the relevant CSV files in the `datasets/` folder. 
3. **Train models:**  
   `python src/train_rf_model.py`  
   `python src/train_dl_model.py`
4. **Run real-time IDS:**  
   `python src/real_time_rf_ids.py`  
   or  
   `python src/real_time_dl_ids.py`

**Note:**
- Feature extraction for live traffic (Scapy) must closely match the dataset. The code uses placeholders—update with your feature extraction logic in `extract(pkt)`.
- Run packet capture scripts as administrator/root if required by your OS.
- Extend scripts for advanced alerting, logging, and visualization as needed.

## Example Output

```
Prediction: 0 | Packet: Ether / IP / TCP 192.168.1.2:12345 > 192.168.1.1:80 S
Prediction: 1 | Packet: Ether / IP / TCP 10.0.0.5:54321 > 10.0.0.1:22 S
```

## License

This project is provided under the MIT License. See [LICENSE](LICENSE) for details.

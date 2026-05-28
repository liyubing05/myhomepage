Title: Projects
Slug: projects

Our group develops high-resolution quantitative ultrasound imaging techniques based on **Full Waveform Inversion (FWI)**, spanning from programmable hardware systems to AI-accelerated algorithms and clinical translation.

---

## 1. Ultrasound Computed Tomography (USCT)

We develop ring-array-based ultrasound computed tomography systems for high-resolution, quantitative imaging of soft tissues. By combining **full matrix capture** with **multi-scale frequency-domain FWI**, we reconstruct sound speed, density, and attenuation maps simultaneously.

**Key achievements:**
- Millimeter-scale resolution (0.4 mm) for musculoskeletal imaging
- First demonstration of 2.5D volumetric reconstruction from ex vivo soft tissues
- Graph-Space Optimal Transport (GSOT) misfit function for robust convergence
- Sobolev space norm regularization balancing low- and high-wavenumber features

**Applications:** Breast cancer screening, musculoskeletal diagnosis, brain imaging.

**Representative publications:** Wu et al., *Ultrasonics*, 2025; Li et al., *Chinese Physics B*, 2025; Wu et al., 仪器仪表学报, 2024.

---

## 2. Programmable Ultrasound Systems

We design and build **GPU-accelerated, programmable ultrasound acquisition systems** that enable arbitrary waveform generation and high-channel-count parallel readout. These systems provide the flexible data acquisition needed for advanced imaging algorithms.

**Key features:**
- 256+ channel parallel acquisition with full matrix capture
- FPGA-based arbitrary waveform generation
- GPU cluster for real-time signal processing
- Open software interface for custom imaging pipelines

---

## 3. AI-Assisted High-Performance Computing for Ultrasound

We leverage deep learning to accelerate wave-equation solvers and inversion workflows:

**Agent-Physics-Informed Neural Networks (APINNs):** A novel architecture that introduces an "agent field" concept to enhance sensitivity to scattered waves. Trained with multi-frequency band strategies, APINNs can directly predict scattered wavefields for arbitrary frequencies within a specified band and reconstruct velocity models with cost only one order of magnitude higher than forward modeling.

**3-D U-Net for Traveltime Picking:** Supervised semantic segmentation approach for automatic first-arrival picking in 3D seismic/ultrasound data, robust to annotation outliers and producing spatially continuous traveltime surfaces.

**Boundary-Enhanced Multimodal Fusion:** Pixel-level fusion of B-mode and elastography ultrasound images for CNN-based classification of benign vs. malignant breast tumors.

**Representative publications:** Dong et al., *Wave Motion*, 2025; Han et al., *IEEE GRSL*, 2022; Li et al., 中国医学影像技术, 2023.

---

## 4. High-Resolution Musculoskeletal Imaging

A dedicated effort to translate USCT technology to clinical musculoskeletal applications. We have developed specialized ring-array probes and inversion algorithms tailored for the high acoustic impedance contrasts present in bone, muscle, and fat tissues.

**Current focus:** High-resolution imaging of extremities (hands, wrists, knees) for early detection of rheumatoid arthritis and osteoporosis.

**Funding:** National Program (PI, 2025–2028); CAS Talent Program (PI, 2024–2026).

**Representative publications:** Wu et al., 仪器仪表学报, 2024; Sun et al., *JASA*, 2025.

---

## 5. Seismic & Geophysical Imaging Methods

Drawing from our group's geophysical roots, we maintain active research in seismic full-waveform inversion and related signal processing:

- **Elastic VTI FWI** with optimal transport misfit for land seismic data
- **Adaptive multiple subtraction** using structure-oriented matched filters
- **Automated well-seismic integration** via spline-based orientation alignment
- **Crosshole GPR tomography** with elliptical anisotropy

These methods developed for geophysical exploration often inspire novel approaches for medical ultrasound imaging.

**Representative publications:** He et al., *Geophysics*, 2023; Sui et al., *Geophysics*, 2024; Ma et al., *Interpretation*, 2024.

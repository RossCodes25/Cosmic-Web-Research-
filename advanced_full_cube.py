import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from itertools import combinations
from data_storage import load_maps_hi, load_params

# === Load data ===
maps_1p_TNG_HI = load_maps_hi()
params = load_params()
maps_per_group = 15

fiducial_params = [0.3, 0.8, 3.6, 1, 7.4, 20]
param_names = ['Ωₘ', 'σ₈', 'A_SN1', 'A_AGN1', 'A_SN2', 'A_AGN2']
omega_m_index = 0  # Focusing on Ωₘ

# === Find test case where only Ωₘ differs ===
def find_fiducial_comparison_cases(param_index, num_cases=1):
    test_cases = []
    used_indices = set()
    for i, j in combinations(range(len(params)), 2):
        if i in used_indices or j in used_indices:
            continue
        other_i = np.delete(params[i, :6], param_index)
        other_j = np.delete(params[j, :6], param_index)
        if np.allclose(other_i, other_j) and not np.isclose(params[i, param_index], params[j, param_index]):
            is_i_fid = np.allclose(params[i, :6], fiducial_params)
            is_j_fid = np.allclose(params[j, :6], fiducial_params)
            if is_i_fid ^ is_j_fid:
                test_cases.append((j, i) if is_i_fid else (i, j))  # (non-fid, fid)
                used_indices.update([i, j])
            if len(test_cases) == num_cases:
                break
    return test_cases

groupA, groupB = find_fiducial_comparison_cases(omega_m_index)[0]

# === Compute residuals for each slice ===
residual_stack = []
for slice_idx in range(maps_per_group):
    idxA = groupA * maps_per_group + slice_idx
    idxB = groupB * maps_per_group + slice_idx
    mapA = maps_1p_TNG_HI[idxA]
    mapB = maps_1p_TNG_HI[idxB]
    log_diff = np.log10(mapA) - np.log10(mapB)
    residual_stack.append(log_diff)

residual_stack = np.array(residual_stack)
avg_residual = np.mean(residual_stack, axis=0)

# === Pick a fiducial slice (e.g., slice 7) for visual comparison ===
fiducial_slice = 6
fid_idx = groupB * maps_per_group + fiducial_slice
fid_map = np.log10(maps_1p_TNG_HI[fid_idx])

# === Plot side-by-side: 3D residuals + 2D HI map ===
fig = make_subplots(
    rows=1, cols=2,
    column_widths=[0.55, 0.45],
    specs=[[{'type': 'surface'}, {'type': 'heatmap'}]],
    subplot_titles=("Mean Residual Over 15 Slices", f"Fiducial HI Map (Slice {fiducial_slice})")
)

# Left: 3D Residual Surface (auto-scaled)
fig.add_trace(go.Surface(
    z=avg_residual,
    colorscale='RdBu',
    colorbar=dict(title="log10 ΔHI", len=0.75, x=0.45)
), row=1, col=1)

# Right: 2D Fiducial HI Map (auto-scaled)
fig.add_trace(go.Heatmap(
    z=fid_map,
    colorscale='Viridis',
    colorbar=dict(title="log10 HI", len=0.75)
), row=1, col=2)

fig.update_layout(
    title_text="Ωₘ Comparison: Residuals vs Fiducial Map",
    height=600,
    margin=dict(t=70, l=20, r=20)
)

fig.show()

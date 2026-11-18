import type {Page} from "@shared/instrument";
import {rect, type Frame} from "@shared/surface";

export function marks(_page: Page, pages: Page[], index: number): Frame {
  const gaps = pages.slice(1,9);
  if (!gaps.length || gaps.some(p=>p.caption!=="FRAME GAP" || !/^\d+(\.\d+)?ms$/.test(p.value))) return [];
  const values = gaps.map(p=>parseFloat(p.value));
  const max = Math.max(0.1,...values);
  return values.map((ms,i)=>{
    const height = Math.max(1,Math.round(8*ms/max));
    return rect("gap"+i,48+i*3,15-height,2,height,i===index-1?"#FFF1D2FF":"#DEA254FF");
  });
}

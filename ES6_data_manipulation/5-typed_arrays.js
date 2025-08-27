export default function createInt8TypedArray(length, position, value) {
  const buffer = new ArrayBuffer(length);
  const int8Array = new Int8Array(buffer);
  if (position > int8Array.length) {
    throw new Error('Position outside of range');
  }
  view[position] = value;
  return new DataView(buffer);
}

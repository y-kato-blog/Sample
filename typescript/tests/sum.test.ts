import { sum } from '../src/sum';

test('basic', () => {
  expect(sum(1, 1)).toBe(2);
});
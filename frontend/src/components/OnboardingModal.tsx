import React, { useState } from 'react';

interface OnboardingModalProps {
  isOpen: boolean;
  onClose: () => void;
  onSubmit: (data: { programmingProficiency: string; aiProficiency: string; hardwareInfo: string }) => void;
}

const OnboardingModal: React.FC<OnboardingModalProps> = ({ isOpen, onClose, onSubmit }) => {
  const [programmingProficiency, setProgrammingProficiency] = useState('');
  const [aiProficiency, setAiProficiency] = useState('');
  const [hardwareInfo, setHardwareInfo] = useState('');

  if (!isOpen) return null;

  const handleSubmit = () => {
    onSubmit({ programmingProficiency, aiProficiency, hardwareInfo });
    onClose();
  };

  return (
    <div className="fixed inset-0 bg-gray-600 bg-opacity-50 flex justify-center items-center">
      <div className="bg-white p-8 rounded-lg shadow-lg w-96">
        <h2 className="text-2xl font-bold mb-4">Welcome! Tell us about yourself</h2>
        <div className="mb-4">
          <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="programmingProficiency">
            Programming Proficiency
          </label>
          <select
            id="programmingProficiency"
            className="shadow border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            value={programmingProficiency}
            onChange={(e) => setProgrammingProficiency(e.target.value)}
          >
            <option value="">Select...</option>
            <option value="Beginner">Beginner</option>
            <option value="Intermediate">Intermediate</option>
            <option value="Expert">Expert</option>
          </select>
        </div>
        <div className="mb-4">
          <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="aiProficiency">
            AI Proficiency
          </label>
          <select
            id="aiProficiency"
            className="shadow border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            value={aiProficiency}
            onChange={(e) => setAiProficiency(e.target.value)}
          >
            <option value="">Select...</option>
            <option value="Beginner">Beginner</option>
            <option value="Intermediate">Intermediate</option>
            <option value="Expert">Expert</option>
          </select>
        </div>
        <div className="mb-6">
          <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="hardwareInfo">
            Hardware Info (e.g., "RTX 3060, 16GB RAM")
          </label>
          <input
            type="text"
            id="hardwareInfo"
            className="shadow border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            value={hardwareInfo}
            onChange={(e) => setHardwareInfo(e.target.value)}
            placeholder="e.g., RTX 3060, 16GB RAM"
          />
        </div>
        <div className="flex items-center justify-between">
          <button
            className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
            type="button"
            onClick={handleSubmit}
          >
            Submit
          </button>
          <button
            className="bg-gray-500 hover:bg-gray-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
            type="button"
            onClick={onClose}
          >
            Cancel
          </button>
        </div>
      </div>
    </div>
  );
};

export default OnboardingModal;
